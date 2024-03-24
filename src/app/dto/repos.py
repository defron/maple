from advanced_alchemy import SQLAlchemyAsyncRepository

from app.dto.entities import Account, Category, Institution, Transaction, TransactionTag


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
    """Account repository."""

    model_type = Transaction
