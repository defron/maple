from dataclasses import dataclass
from decimal import Decimal

from app.dto.entities import AccountType, Category
from app.enums.enums import TransactionType


@dataclass
class BalanceChange:
    inflow: Decimal = Decimal(0)
    outflow: Decimal = Decimal(0)
    transfer_in: Decimal = Decimal(0)
    transfer_out: Decimal = Decimal(0)


def balance_change_helper(
    account_type: AccountType, amount: Decimal, txn_type: TransactionType, category: Category
) -> BalanceChange:
    bal = BalanceChange()
    if account_type.is_asset:
        # TODO: hardcoding transfer ID for now, should revisit
        if txn_type == TransactionType.Debit and category.id is not 14 and category.parent_category_id is not 14:
            bal.inflow = amount
        elif txn_type == TransactionType.Debit:
            bal.transfer_in = amount
        elif txn_type == TransactionType.Credit and category.id is not 14 and category.parent_category_id is not 14:
            bal.outflow = amount
        else:
            bal.transfer_out = amount
    else:
        if txn_type == TransactionType.Credit:
            bal.outflow = amount
        else:
            bal.transfer_in = amount
    return bal
