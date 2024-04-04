from decimal import Decimal

from app.dto.entities import Account, AccountType, Cashflow, Category
from app.enums.enums import TransactionType


def balance_change_helper(
    cashflow: Cashflow, account_type: AccountType, amount: Decimal, txn_type: TransactionType, category: Category
) -> Cashflow:
    if account_type.is_asset:
        if txn_type == TransactionType.Debit and category.is_cashflow:
            cashflow.inflow = amount + (cashflow.inflow or Decimal(0))
        elif txn_type == TransactionType.Debit:
            cashflow.transfer_in = amount + (cashflow.transfer_in or Decimal(0))
        elif category.is_cashflow:
            cashflow.outflow = amount + (cashflow.outflow or Decimal(0))
        else:
            cashflow.transfer_out = amount + (cashflow.transfer_out or Decimal(0))
    else:
        if txn_type == TransactionType.Credit and category.is_cashflow:
            cashflow.outflow = amount + (cashflow.outflow or Decimal(0))
        elif txn_type == TransactionType.Credit:
            cashflow.transfer_out = amount + (cashflow.transfer_out or Decimal(0))
        # the only time I could see this happening is a redemption on a credit card or something alone those lines
        elif category.is_cashflow:
            cashflow.inflow = amount + (cashflow.inflow or Decimal(0))
        else:
            cashflow.transfer_in = amount + (cashflow.transfer_in or Decimal(0))
    return cashflow


def updated_balance(account: Account, change: Decimal, txn_type: TransactionType) -> Decimal:
    if account.account_type.is_asset:
        if txn_type == TransactionType.Debit:
            account.balance += change
        else:
            account.balance -= change
    else:
        if txn_type == TransactionType.Credit:
            account.balance += change
        else:
            account.balance -= change
    return account.balance
