CREATE SCHEMA IF NOT EXISTS maple;

CREATE TABLE IF NOT EXISTS maple.app (
	id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
	version VARCHAR(20) NOT NULL,
    app_metadata JSONB,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.user (
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    pass_hash TEXT NOT NULL,
    salt  CHAR(32) NOT NULL,
    user_metadata JSONB,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.txn_source (
	id uuid PRIMARY KEY,
	name VARCHAR(255) UNIQUE NOT NULL,
    has_api BOOLEAN NOT NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.timespan (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) UNIQUE NOT NULL,
    span INTERVAL NOT NULL,
    allowed_for_budget BOOLEAN NOT NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (1, 'Monthly', '1 month', TRUE);

CREATE TABLE IF NOT EXISTS maple.acct_auth (
	id SERIAL PRIMARY KEY,
	external_auth_id VARCHAR(255),
    external_source_metadata JSONB,
    external_reauth_required BOOLEAN NOT NULL DEFAULT FALSE,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.institution (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
    logo TEXT,
    url TEXT,
    external_institution_id VARCHAR(255),
    external_source_metadata JSONB,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.account_type (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
    is_asset BOOLEAN NOT NULL DEFAULT TRUE,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.tag (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.category (
	id SERIAL PRIMARY KEY,
	name VARCHAR(128) UNIQUE NOT NULL,
    logo TEXT,
    is_hidden BOOLEAN NOT NULL DEFAULT FALSE,
    parent_category_id INT REFERENCES maple.category(id) ON DELETE SET NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (1, 'Uncategorized', NULL);

CREATE TABLE IF NOT EXISTS maple.account (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
    account_type_id INT NOT NULL REFERENCES maple.account_type(id) ON DELETE CASCADE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    external_txn_cursor_id VARCHAR(255),
    external_last_request_id VARCHAR(255),
    balance NUMERIC(14,4) NOT NULL,
    account_limit NUMERIC(14,4),
    is_inverted BOOLEAN NOT NULL DEFAULT FALSE,
    institution_id INT REFERENCES maple.institution(id) ON DELETE SET NULL,
    auth_id INT REFERENCES maple.acct_auth(id) ON DELETE SET NULL,
    external_account_id VARCHAR(255),
    currency_code CHAR(3) NOT NULL DEFAULT 'USD',
    acct_num_masked VARCHAR(255),
    external_account_metadata JSONB,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.bill (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
    url TEXT,
    timespan_id INT NOT NULL REFERENCES maple.timespan(id) ON DELETE CASCADE,
    is_dynamic BOOLEAN NOT NULL DEFAULT TRUE,
    static_amount NUMERIC(14,4) NOT NULL DEFAULT 0,
    account_id INT REFERENCES maple.account(id) ON DELETE SET NULL,
    is_past_due BOOLEAN NOT NULL DEFAULT FALSE,
	next_statement_date DATE NOT NULL,
	next_due_date DATE NOT NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.historical_account_balance (
	id SERIAL PRIMARY KEY,
	account_id INT REFERENCES maple.account(id) ON DELETE CASCADE,
	balance_date DATE NOT NULL DEFAULT CURRENT_DATE,
    balance NUMERIC(14,4) NOT NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.cashflow (
	id SERIAL PRIMARY KEY,
	account_id INT NOT NULL REFERENCES maple.account(id) ON DELETE CASCADE,
	time_period DATE NOT NULL,
    inflow NUMERIC(14,4) NOT NULL DEFAULT 0,
    outflow NUMERIC(14,4) NOT NULL DEFAULT 0,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.investment_purchase (
	id BIGSERIAL PRIMARY KEY,
	account_id INT NOT NULL REFERENCES maple.account(id) ON DELETE CASCADE,
	ticker VARCHAR(30) NOT NULL,
    purchase_date DATE NOT NULL,
    individual_purchase_price NUMERIC(11,4) NOT NULL,
    purchase_quantity NUMERIC(11,4) NOT NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.investment_sale (
	id BIGSERIAL PRIMARY KEY,
	investment_purchase_id BIGINT NOT NULL REFERENCES maple.investment_purchase(id) ON DELETE CASCADE,
    sale_date DATE NOT NULL,
    individual_sale_price NUMERIC(11,4) NOT NULL,
    sale_quantity NUMERIC(11,4) NOT NULL,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.account_txn_rule (
	id SERIAL PRIMARY KEY,
	account_id INT NOT NULL REFERENCES maple.account(id) ON DELETE CASCADE,
	name VARCHAR(255) NOT NULL,
    new_category_id INT REFERENCES maple.category(id) ON DELETE CASCADE,
    additional_tag_id INT REFERENCES maple.tag(id) ON DELETE SET NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    rule_json JSONB,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.transaction (
	id BIGSERIAL PRIMARY KEY,
	description VARCHAR(4096),
    amount NUMERIC(11,4) NOT NULL,
    account_id INT NOT NULL REFERENCES maple.account(id) ON DELETE CASCADE,
    category_id INT NOT NULL REFERENCES maple.category(id) ON DELETE RESTRICT,
    payed_bill_id INT REFERENCES maple.bill(id) ON DELETE SET NULL,
    merchant_category_code VARCHAR(255),
    txn_date DATE NOT NULL,
    external_merchant_id VARCHAR(255),
    custom_merchant_name VARCHAR(255),
    original_merchant_name VARCHAR(255),
    merchant_url TEXT,
    custom_note VARCHAR(4096),
    original_note VARCHAR(4096),
    txn_source_id uuid REFERENCES maple.txn_source(id) ON DELETE SET NULL,
    soft_delete BOOLEAN NOT NULL DEFAULT FALSE,
    is_pending BOOLEAN NOT NULL DEFAULT FALSE,
    hash_and_daycount CHAR(67) NOT NULL,
    source_metadata JSONB,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.subtransaction (
	id BIGSERIAL PRIMARY KEY,
    txn_id BIGINT NOT NULL REFERENCES maple.transaction(id) ON DELETE CASCADE,
    description VARCHAR(4096),
    amount NUMERIC(11,4) NOT NULL,
    category_id INT NOT NULL REFERENCES maple.category(id) ON DELETE RESTRICT,
    custom_note VARCHAR(4096),
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.txn_tags (
	id SERIAL PRIMARY KEY,
    tag_id INT NOT NULL REFERENCES maple.tag(id) ON DELETE CASCADE,
    txn_id BIGINT NOT NULL REFERENCES maple.transaction(id) ON DELETE CASCADE,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS maple.budget (
	id SERIAL PRIMARY KEY,
    category_id INT NOT NULL REFERENCES maple.category(id) ON DELETE RESTRICT,
    amount NUMERIC(11,4) NOT NULL,
    effective_date DATE NOT NULL,
    end_date DATE,
    timespan_id INT NOT NULL REFERENCES maple.timespan(id) ON DELETE RESTRICT,
    show_always BOOLEAN NOT NULL DEFAULT TRUE,
    prorate BOOLEAN NOT NULL DEFAULT FALSE,
	created_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_dt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);