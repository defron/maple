import decimal
from datetime import datetime
from typing import Any

from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


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


class AccountRequestModel(BaseModel):
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


class AccountTypeResponseModel(BaseModel):
    id: int
    name: str
    is_asset: bool
    created_dt: datetime
    updated_dt: datetime


class UpdateAccountRequestModel(BaseModel):
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


class AccountResponseModel(BaseModel):
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
