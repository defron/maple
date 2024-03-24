import decimal
import hashlib
from datetime import date


def transaction_hash(date: date, amount: decimal.Decimal, type: str, label: str) -> str:
    important_data = [date.strftime("%Y-%m-%d"), str(amount), type, label]
    return hashlib.sha256("|".join(important_data).encode("utf-8")).hexdigest()
