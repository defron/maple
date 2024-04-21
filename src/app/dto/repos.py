from advanced_alchemy import SQLAlchemyAsyncRepository

from app.dto.entities import Account, Budget, Cashflow, Category, Institution, Subtransaction, Transaction, TransactionTag


class InstitutionRepository(SQLAlchemyAsyncRepository[Institution]): # pyright: ignore
    """Instittuion repository."""

    model_type = Institution


class TagRepository(SQLAlchemyAsyncRepository[TransactionTag]): # pyright: ignore
    """Tag repository."""

    model_type = TransactionTag


class CategoryRepository(SQLAlchemyAsyncRepository[Category]): # pyright: ignore
    """Category repository."""

    model_type = Category


class AccountRepository(SQLAlchemyAsyncRepository[Account]): # pyright: ignore
    """Account repository."""

    model_type = Account


class TransactionRepository(SQLAlchemyAsyncRepository[Transaction]): # pyright: ignore
    """Transaction repository."""

    model_type = Transaction


class SubtransactionRepository(SQLAlchemyAsyncRepository[Subtransaction]): # pyright: ignore
    """Subtransaction repository."""

    model_type = Subtransaction


class CashflowRepository(SQLAlchemyAsyncRepository[Cashflow]): # pyright: ignore
    """Cashflow repository."""

    model_type = Cashflow

class BudgetRepository(SQLAlchemyAsyncRepository[Budget]): # pyright: ignore
    """Budget repository."""

    model_type = Budget