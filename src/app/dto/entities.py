import datetime
import decimal
import uuid
from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import Interval, BigInteger, Text
from sqlalchemy.dialects.postgresql import JSONB
from typing import Any


class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, Any]: JSONB
    }

class AccountType(Base):
    __tablename__ = "account_type"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    is_asset: Mapped[bool]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class App(Base):
    __tablename__ = "app"
    id: Mapped[int] = mapped_column(primary_key=True)
    version: Mapped[str]
    app_metadata: Mapped[dict[str, Any]]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    pass_hash: Mapped[str] = mapped_column(Text)
    salt: Mapped[str]
    user_metadata: Mapped[dict[str, Any]]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class TransactionSource(Base):
    __tablename__ = "txn_source"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    has_api: Mapped[bool]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class TimeSpan(Base):
    __tablename__ = "timespan"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    span: Mapped[datetime.timedelta] = mapped_column(Interval)
    allowed_for_budget: Mapped[bool]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class AccountAuth(Base):
    __tablename__ = "acct_auth"
    id: Mapped[int] = mapped_column(primary_key=True)
    external_auth_id: Mapped[str]
    external_source_metadata: Mapped[dict[str, Any]]
    external_reauth_required: Mapped[bool]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Institution(Base):
    __tablename__ = "institution"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    logo: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text)
    external_institution_id: Mapped[str]
    external_source_metadata: Mapped[dict[str, Any]]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class TransactionTag(Base):
    __tablename__ = "tag"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    logo: Mapped[str] = mapped_column(Text)
    is_hidden: Mapped[bool]
    parent_category_id: Mapped[bool] = mapped_column(ForeignKey("category.id"))
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Account(Base):
    __tablename__ = "account"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_type_id: Mapped[int] = mapped_column(ForeignKey("account_type.id"))
    is_active: Mapped[bool]
    external_txn_cursor_id: Mapped[str]
    external_last_request_id: Mapped[str]
    balance: Mapped[decimal.Decimal] = mapped_column(Numeric(14,4), nullable=False)
    account_limit: Mapped[decimal.Decimal] = mapped_column(Numeric(14,4), nullable=True)
    is_inverted: Mapped[bool]
    institution_id: Mapped[int] = mapped_column(ForeignKey("institution.id"))
    auth_id: Mapped[int] = mapped_column(ForeignKey("acct_auth.id"))
    external_account_id: Mapped[str]
    currency_code: Mapped[str]
    acct_num_masked: Mapped[str]
    external_account_metadata: Mapped[dict[str, Any]]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Bill(Base):
    __tablename__ = "bill"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str] = mapped_column(Text)
    interval_id: Mapped[int] = mapped_column(ForeignKey("interval.id"))
    is_dynamic: Mapped[bool]
    static_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(14,4), nullable=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    is_past_due: Mapped[bool]
    next_statement_date: Mapped[datetime.date]
    next_due_date: Mapped[datetime.date]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class HistoricalAccountBalance(Base):
    __tablename__ = "historical_account_balance"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    balance_date: Mapped[datetime.date]
    balance: Mapped[decimal.Decimal] = mapped_column(Numeric(14,4), nullable=False)
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Cashflow(Base):
    __tablename__ = "cashflow"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    time_period: Mapped[datetime.date]
    inflow: Mapped[decimal.Decimal] = mapped_column(Numeric(14,4), nullable=False)
    outflow: Mapped[decimal.Decimal] = mapped_column(Numeric(14,4), nullable=False)
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class InvestmentPurchase(Base):
    __tablename__ = "investment_purchase"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    ticker: Mapped[str]
    purchase_date: Mapped[datetime.date]
    individual_purchase_price: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    purchase_quantity: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class InvestmentSale(Base):
    __tablename__ = "investment_sale"
    id: Mapped[int] = mapped_column(primary_key=True)
    investment_purchase_id: Mapped[int] = mapped_column(ForeignKey("investment_purchase.id"))
    sale_date: Mapped[datetime.date]
    individual_sale_price: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    sale_quantity: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class AccountTransactionRule(Base):
    __tablename__ = "account_txn_rule"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    name: Mapped[str]
    new_category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    additional_tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))
    is_active: Mapped[bool]
    rule_json: Mapped[dict[str, Any]]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Transaction(Base):
    __tablename__ = "transaction"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    description: Mapped[str]
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    payed_bill_id: Mapped[int] = mapped_column(ForeignKey("bill.id"))
    merchant_category_code: Mapped[str]
    txn_date: Mapped[datetime.date]
    external_merchant_id: Mapped[str]
    custom_merchant_name: Mapped[str]
    original_merchant_name: Mapped[str]
    merchant_url: Mapped[str] = mapped_column(Text)
    custom_note: Mapped[str]
    original_note: Mapped[str]
    txn_source_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(""))
    soft_delete: Mapped[bool]
    is_pending: Mapped[bool]
    hash_and_daycount: Mapped[str]
    source_metadata: Mapped[dict[str, Any]]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class Subtransaction(Base):
    __tablename__ = "subtransaction"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    txn_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("transaction.id"))
    description: Mapped[str]
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    custom_note: Mapped[str]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

class TransactionTags(Base):
    __tablename__ = "txn_tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))
    txn_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("transaction.id"))
    created_dt: Mapped[datetime.datetime]

class Budget(Base):
    __tablename__ = "budget"
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(11,4), nullable=False)
    effective_date: Mapped[datetime.date]
    interval_id: Mapped[int] = mapped_column(ForeignKey("interval.id"), nullable=False, default=1)
    show_always: Mapped[bool]
    prorate: Mapped[bool]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]

