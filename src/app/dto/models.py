import decimal
from datetime import datetime
from typing import Any

from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from pydantic import BaseModel

from app.dto.entities import Account


class Base(BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


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
    parent_category_id: int | None


class CategoryResponseModel(Base):
    id: int
    name: str
    logo: str | None
    is_hidden: bool
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
