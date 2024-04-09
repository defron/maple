import decimal
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any

from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.datastructures import UploadFile
from pydantic import BaseModel

from app.dto.entities import Account, Transaction
from app.enums.enums import DateFormatFirstSegment


class Base(BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


class UploadBase(BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True, "arbitrary_types_allowed": True}


class InstitutionRequestModel(Base):
    name: str
    logo: str | None
    url: str | None
    external_institution_id: str | None
    external_source_metadata: dict[str, Any] | None


class InstitutionResponseModel(Base):
    id: int
    name: str
    logo: str | None
    url: str | None
    external_institution_id: str | None
    external_source_metadata: dict[str, Any] | None
    created_dt: datetime
    updated_dt: datetime


class CategoryRequestModel(Base):
    name: str
    logo: str | None
    is_hidden: bool
    is_cashflow: bool
    parent_category_id: int | None


class CategoryResponseModel(Base):
    id: int
    name: str
    logo: str | None
    is_protected: bool
    is_hidden: bool
    is_cashflow: bool
    parent_category_id: int | None
    created_dt: datetime
    updated_dt: datetime


class TagRequestModel(Base):
    name: str


class TagResponseModel(Base):
    id: int
    name: str
    created_dt: datetime
    updated_dt: datetime


class AccountRequestModel(Base):
    name: str
    account_type_id: int
    external_txn_cursor_id: str | None
    external_last_request_id: str | None
    balance: decimal.Decimal
    account_limit: decimal.Decimal | None
    is_inverted: bool
    institution_id: int
    auth_id: int | None
    external_account_id: str | None
    currency_code: str
    acct_num_masked: str | None
    external_account_metadata: dict[str, Any] | None


class AccountTypeResponseModel(Base):
    id: int
    name: str
    is_asset: bool
    created_dt: datetime
    updated_dt: datetime


class UpdateAccountRequestModel(Base):
    name: str
    account_type_id: int
    is_active: bool
    external_txn_cursor_id: str | None
    external_last_request_id: str | None
    balance: decimal.Decimal
    account_limit: decimal.Decimal | None
    is_inverted: bool
    institution_id: int
    auth_id: int | None
    external_account_id: str | None
    currency_code: str
    acct_num_masked: str | None
    external_account_metadata: dict[str, Any] | None


class AccountResponseModel(Base):
    id: int
    name: str
    account_type_id: int
    account_type: AccountTypeResponseModel | None
    is_active: bool
    external_txn_cursor_id: str | None
    external_last_request_id: str | None
    balance: decimal.Decimal
    account_limit: decimal.Decimal | None
    is_inverted: bool
    institution_id: int
    auth_id: int | None
    external_account_id: str | None
    currency_code: str
    acct_num_masked: str | None
    external_account_metadata: dict[str, Any] | None
    created_dt: datetime
    updated_dt: datetime


class AccountDTO(SQLAlchemyDTO[Account]):
    config = SQLAlchemyDTOConfig(
        exclude={
            "transactions",
            "transaction_rules",
            "holdings",
            "monthly_cashflows",
            "historical_balances",
            "bills",
            "authentication",
            "institution",
        }
    )


class ManualTransactionRequest(Base):
    label: str | None
    amount: decimal.Decimal
    txn_type: str
    account_id: int
    category_id: int
    payed_bill_id: int | None
    txn_date: date
    original_merchant_name: str | None
    merchant_url: str | None
    original_note: str | None
    update_balance: bool


class UpdateTransactionRequest(Base):
    category_id: int
    payed_bill_id: int | None
    txn_date: date | None
    custom_merchant_name: str | None
    merchant_url: str | None
    custom_note: str | None
    soft_delete: bool | None


class SubtransactionRequest(Base):
    description: str
    amount: decimal.Decimal
    category_id: int
    custom_note: str | None


class TransactionDTO(SQLAlchemyDTO[Transaction]):
    config = SQLAlchemyDTOConfig(
        exclude={
            "account",
            "paid_bill",
            "transaction_source",
            "tag_associations",
            "category.subcategories",
        },
        max_nested_depth=2,
    )


@dataclass
class CsvTransactionsRequest:
    account_id: int
    label_field: str | None
    amount_field: str
    txn_type_from_sign: bool
    txn_type_field_name: str
    txn_type_credit_value: str
    category_field: str | None
    category_mapping: str | None
    txn_date_field: str
    txn_date_parse_preference: DateFormatFirstSegment
    note_field: str | None
    external_txn_id_field: str | None
    file: UploadFile
    update_balance_after: date | None
