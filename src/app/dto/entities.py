import decimal
import uuid
from datetime import date, datetime, timedelta
from typing import Any, List, Optional

from advanced_alchemy import SQLAlchemyAsyncRepository
from advanced_alchemy.base import CommonTableAttributes, orm_registry
from litestar.dto import dto_field
from pydantic import BaseModel as _BaseModel
from sqlalchemy import CHAR, UUID, Boolean, Date, DateTime, ForeignKey, Integer, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import BigInteger, Interval, Text


class Base(CommonTableAttributes, DeclarativeBase):
    registry = orm_registry


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


class App(Base):
    __tablename__ = "app"  #  type: ignore[assignment]
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    version: Mapped[str] = mapped_column(String(length=20), nullable=False)
    app_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = "user"  #  type: ignore[assignment]
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    username: Mapped[str] = mapped_column(String(length=30), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    email: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    pass_hash: Mapped[str] = mapped_column(Text, nullable=False)
    salt: Mapped[str] = mapped_column(CHAR(length=32), nullable=False)
    user_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class TransactionSource(Base):
    __tablename__ = "txn_source"  #  type: ignore[assignment]
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    has_api: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    transactions: Mapped[List["Transaction"]] = relationship(
        back_populates="transaction_source", lazy="noload", info=dto_field("private")
    )


class TimeSpan(Base):
    __tablename__ = "timespan"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, info=dto_field("read-only"))
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    span: Mapped[timedelta] = mapped_column(Interval, nullable=False)
    allowed_for_budget: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_dt: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), info=dto_field("read-only")
    )
    updated_dt: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), info=dto_field("read-only")
    )
    bills: Mapped[List["Bill"]] = relationship(back_populates="timespan", lazy="noload", info=dto_field("private"))
    budgets: Mapped[List["Budget"]] = relationship(back_populates="timespan", lazy="noload", info=dto_field("private"))


class AccountAuth(Base):
    __tablename__ = "acct_auth"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    external_auth_id: Mapped[str] = mapped_column(String(length=255))
    external_source_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB, info=dto_field("private"))
    external_reauth_required: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("FALSE")
    )
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    accounts: Mapped[List["Account"]] = relationship(back_populates="authentication", lazy="noload")


class Institution(Base):
    __tablename__ = "institution"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, info=dto_field("read-only"))
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    logo: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text)
    external_institution_id: Mapped[str] = mapped_column(String(length=255))
    external_source_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_dt: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), info=dto_field("read-only")
    )
    updated_dt: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), info=dto_field("read-only")
    )
    accounts: Mapped[List["Account"]] = relationship(back_populates="institution", info=dto_field("private"))


class InstitutionRequestModel(BaseModel):
    name: str
    logo: str | None
    url: str | None
    external_institution_id: str | None
    external_source_metadata: dict[str, Any] | None


class InstitutionResponseModel(BaseModel):
    id: int
    name: str
    logo: str | None
    url: str | None
    external_institution_id: str | None
    external_source_metadata: dict[str, Any] | None
    created_dt: datetime
    updated_dt: datetime


class CategoryRequestModel(BaseModel):
    name: str
    logo: str | None
    is_hidden: bool
    parent_category_id: int | None


class CategoryResponseModel(BaseModel):
    id: int
    name: str
    logo: str | None
    is_hidden: bool
    parent_category_id: int | None
    created_dt: datetime
    updated_dt: datetime


class TagRequestModel(BaseModel):
    name: str


class TagResponseModel(BaseModel):
    id: int
    name: str
    created_dt: datetime
    updated_dt: datetime


class InstitutionRepository(SQLAlchemyAsyncRepository[Institution]):
    """Instittuion repository."""

    model_type = Institution


class AccountType(Base):
    __tablename__ = "account_type"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    is_asset: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("TRUE"))
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    accounts: Mapped[List["Account"]] = relationship(
        back_populates="account_type", lazy="noload", info=dto_field("private")
    )


class TransactionTag(Base):
    __tablename__ = "tag"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    apply_via_transaction_rules: Mapped[List["AccountTransactionRule"]] = relationship(
        back_populates="apply_tag", lazy="noload"
    )
    transactions: Mapped[List["Transaction"]] = relationship(
        secondary="txn_tags", back_populates="tags", lazy="noload", viewonly=True, info=dto_field("private")
    )
    transaction_associations: Mapped[List["TransactionTags"]] = relationship(
        back_populates="transaction_tag", lazy="noload", viewonly=True, info=dto_field("private")
    )


class TagRepository(SQLAlchemyAsyncRepository[TransactionTag]):
    """Tag repository."""

    model_type = TransactionTag


class Category(Base):
    __tablename__ = "category"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    logo: Mapped[str] = mapped_column(Text)
    is_hidden: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("FALSE"))
    parent_category_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("category.id", ondelete="SET NULL"))
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    parent_category: Mapped[Optional["Category"]] = relationship(
        back_populates="subcategories", remote_side=[id], info=dto_field("private")
    )
    subcategories: Mapped[List["Category"]] = relationship(
        back_populates="parent_category", order_by="Category.id", lazy="select", viewonly=True
    )
    change_category_rules: Mapped[List["AccountTransactionRule"]] = relationship(
        back_populates="new_category", info=dto_field("private")
    )
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="category", info=dto_field("private"))
    subtransactions: Mapped[List["Subtransaction"]] = relationship(
        back_populates="category", info=dto_field("private")
    )
    budgets: Mapped[List["Budget"]] = relationship(back_populates="category", info=dto_field("private"))


class CategoryRepository(SQLAlchemyAsyncRepository[Category]):
    """Tag repository."""

    model_type = Category


class Account(Base):
    __tablename__ = "account"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    account_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("account_type.id", ondelete="CASCADE"), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("TRUE"))
    external_txn_cursor_id: Mapped[str] = mapped_column(String(length=255))
    external_last_request_id: Mapped[str] = mapped_column(String(length=255))
    balance: Mapped[decimal.Decimal] = mapped_column(Numeric(14, 4), nullable=False)
    account_limit: Mapped[decimal.Decimal] = mapped_column(Numeric(14, 4), nullable=True)
    is_inverted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("FALSE"))
    institution_id: Mapped[int] = mapped_column(Integer, ForeignKey("institution.id", ondelete="SET NULL"))
    auth_id: Mapped[int] = mapped_column(Integer, ForeignKey("acct_auth.id", ondelete="SET NULL"))
    external_account_id: Mapped[str] = mapped_column(String(length=255))
    currency_code: Mapped[str] = mapped_column(CHAR(length=3), nullable=False, server_default="USD")
    acct_num_masked: Mapped[str] = mapped_column(String(length=255))
    external_account_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account_type: Mapped["AccountType"] = relationship(back_populates="accounts", lazy="select")
    institution: Mapped[Optional["Institution"]] = relationship(back_populates="accounts", lazy="select")
    authentication: Mapped[Optional["AccountAuth"]] = relationship(back_populates="accounts", lazy="noload")
    bills: Mapped[List["Bill"]] = relationship(back_populates="account", lazy="select")
    historical_balances: Mapped[List["HistoricalAccountBalance"]] = relationship(
        back_populates="account", lazy="noload"
    )
    monthly_cashflows: Mapped[List["Cashflow"]] = relationship(back_populates="account", lazy="noload")
    holdings: Mapped[List["InvestmentPurchase"]] = relationship(back_populates="account", lazy="noload")
    transaction_rules: Mapped[List["AccountTransactionRule"]] = relationship(back_populates="account", lazy="select")
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="account", lazy="noload")


class Bill(Base):
    __tablename__ = "bill"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    url: Mapped[str] = mapped_column(Text)
    timespan_id: Mapped[int] = mapped_column(Integer, ForeignKey("timespan.id", ondelete="CASCADE"), nullable=False)
    is_dynamic: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("TRUE"))
    static_amount: Mapped[decimal.Decimal] = mapped_column(
        Numeric(14, 4), nullable=True, default=0, server_default=text("0")
    )
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("account.id", ondelete="SET NULL"))
    is_past_due: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("FALSE"))
    next_statement_date: Mapped[date] = mapped_column(Date, nullable=False)
    next_due_date: Mapped[date] = mapped_column(Date, nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    timespan: Mapped["TimeSpan"] = relationship(back_populates="bills", lazy="noload")
    account: Mapped[Optional["Account"]] = relationship(back_populates="bills", lazy="noload")
    paid_bill_transactions: Mapped[List["Transaction"]] = relationship(back_populates="paid_bill", lazy="noload")


class HistoricalAccountBalance(Base):
    __tablename__ = "historical_account_balance"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("account.id", ondelete="CASCADE"))
    balance_date: Mapped[date] = mapped_column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    balance: Mapped[decimal.Decimal] = mapped_column(Numeric(14, 4), nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account: Mapped["Account"] = relationship(back_populates="historical_balances", lazy="noload")


class Cashflow(Base):
    __tablename__ = "cashflow"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("account.id", ondelete="CASCADE"), nullable=False)
    time_period: Mapped[date] = mapped_column(Date, nullable=False)
    inflow: Mapped[decimal.Decimal] = mapped_column(
        Numeric(14, 4), nullable=False, default=decimal.Decimal("0"), server_default=text("0")
    )
    outflow: Mapped[decimal.Decimal] = mapped_column(
        Numeric(14, 4), nullable=False, default=decimal.Decimal("0"), server_default=text("0")
    )
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account: Mapped["Account"] = relationship(back_populates="monthly_cashflows", lazy="noload")


class InvestmentPurchase(Base):
    __tablename__ = "investment_purchase"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("account.id", ondelete="CASCADE"), nullable=False)
    ticker: Mapped[str] = mapped_column(String(length=30), nullable=False)
    purchase_date: Mapped[date] = mapped_column(Date, nullable=False)
    individual_purchase_price: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    purchase_quantity: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account: Mapped["Account"] = relationship(back_populates="holdings", lazy="noload")
    sales: Mapped[List["InvestmentSale"]] = relationship(back_populates="associated_purchase", lazy="noload")


class InvestmentSale(Base):
    __tablename__ = "investment_sale"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    investment_purchase_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("investment_purchase.id", ondelete="CASCADE"), nullable=False
    )
    sale_date: Mapped[date] = mapped_column(Date, nullable=False)
    individual_sale_price: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    sale_quantity: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    associated_purchase: Mapped["InvestmentPurchase"] = relationship(back_populates="sales", lazy="noload")


class AccountTransactionRule(Base):
    __tablename__ = "account_txn_rule"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("account.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(length=30), nullable=False)
    new_category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    additional_tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tag.id", ondelete="SET NULL"))
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("TRUE"))
    rule_json: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    new_category: Mapped[Optional["Category"]] = relationship(back_populates="change_category_rules", lazy="noload")
    account: Mapped["Account"] = relationship(back_populates="transaction_rules", lazy="noload")
    apply_tag: Mapped[Optional["TransactionTag"]] = relationship(
        back_populates="apply_via_transaction_rules", lazy="noload"
    )


class Transaction(Base):
    __tablename__ = "transaction"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    description: Mapped[str] = mapped_column(String(length=4096))
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("account.id", ondelete="CASCADE"), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id", ondelete="RESTRICT"), nullable=False)
    payed_bill_id: Mapped[int] = mapped_column(Integer, ForeignKey("bill.id", ondelete="SET NULL"))
    merchant_category_code: Mapped[str] = mapped_column(String(length=255))
    txn_date: Mapped[date] = mapped_column(Date, nullable=False)
    external_merchant_id: Mapped[str] = mapped_column(String(length=255))
    custom_merchant_name: Mapped[str] = mapped_column(String(length=255))
    original_merchant_name: Mapped[str] = mapped_column(String(length=255))
    merchant_url: Mapped[str] = mapped_column(Text)
    custom_note: Mapped[str] = mapped_column(String(length=4096))
    original_note: Mapped[str] = mapped_column(String(length=4096))
    txn_source_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("txn_source.id", ondelete="SET NULL"))
    soft_delete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("FALSE"))
    is_pending: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("FALSE"))
    hash_and_daycount: Mapped[str] = mapped_column(CHAR(length=67), nullable=False)
    source_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account: Mapped["Account"] = relationship(back_populates="transactions", lazy="noload")
    category: Mapped["Category"] = relationship(back_populates="transactions", lazy="noload")
    paid_bill: Mapped[Optional["Bill"]] = relationship(back_populates="paid_bill_transactions", lazy="noload")
    transaction_source: Mapped[Optional["TransactionSource"]] = relationship(
        back_populates="transactions", lazy="noload"
    )
    subtransactions: Mapped[List["Subtransaction"]] = relationship(back_populates="split_transaction", lazy="noload")
    tags: Mapped[List["TransactionTag"]] = relationship(
        secondary="txn_tags", back_populates="transactions", lazy="noload"
    )
    tag_associations: Mapped[List["TransactionTags"]] = relationship(
        back_populates="transaction", viewonly=True, lazy="noload"
    )


class Subtransaction(Base):
    __tablename__ = "subtransaction"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    txn_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("transaction.id", ondelete="CASCADE"), nullable=False)
    description: Mapped[str] = mapped_column(String(length=4096))
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id", ondelete="RESTRICT"), nullable=False)
    custom_note: Mapped[str] = mapped_column(String(length=4096))
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    category: Mapped["Category"] = relationship(back_populates="subtransactions", lazy="noload")
    split_transaction: Mapped["Transaction"] = relationship(back_populates="subtransactions", lazy="noload")


class TransactionTags(Base):
    __tablename__ = "txn_tags"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id", ondelete="CASCADE"), nullable=False)
    txn_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("transaction.id", ondelete="CASCADE"), nullable=False)
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    transaction_tag: Mapped["TransactionTag"] = relationship(
        back_populates="transaction_associations", viewonly=True, lazy="noload"
    )
    transaction: Mapped["Transaction"] = relationship(back_populates="tag_associations", viewonly=True, lazy="noload")


class Budget(Base):
    __tablename__ = "budget"  #  type: ignore[assignment]
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id", ondelete="RESTRICT"), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(11, 4), nullable=False)
    effective_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=True)
    timespan_id: Mapped[int] = mapped_column(Integer, ForeignKey("timespan.id", ondelete="RESTRICT"), nullable=False)
    show_always: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("TRUE"))
    prorate: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("FALSE"))
    created_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_dt: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    timespan: Mapped["TimeSpan"] = relationship(back_populates="budgets", lazy="noload")
    category: Mapped["Category"] = relationship(back_populates="budgets", lazy="noload")
