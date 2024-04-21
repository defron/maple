from advanced_alchemy import SQLAlchemyAsyncRepository

from app.dto.entities import Account, Budget, Cashflow, Category, Institution, Subtransaction, Transaction, TransactionTag


class InstitutionRepository(SQLAlchemyAsyncRepository[Institution]):
    """Instittuion repository."""

    model_type = Institution


class TagRepository(SQLAlchemyAsyncRepository[TransactionTag]):
    """Tag repository."""

    model_type = TransactionTag


class CategoryRepository(SQLAlchemyAsyncRepository[Category]):
    """Category repository."""

    model_type = Category


class AccountRepository(SQLAlchemyAsyncRepository[Account]):
    """Account repository."""

    model_type = Account


class TransactionRepository(SQLAlchemyAsyncRepository[Transaction]):
    """Transaction repository."""

    model_type = Transaction


class SubtransactionRepository(SQLAlchemyAsyncRepository[Subtransaction]):
    """Subtransaction repository."""

    model_type = Subtransaction


class CashflowRepository(SQLAlchemyAsyncRepository[Cashflow]):
    """Cashflow repository."""

    model_type = Cashflow

class BudgetRepository(SQLAlchemyAsyncRepository[Budget]):
    """Budget repository."""

    model_type = Budget