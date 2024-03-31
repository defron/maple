from enum import Enum


class DateFormatFirstSegment(Enum):
    Month = "MONTH"
    Day = "DAY"
    Year = "YEAR"


class TransactionType(Enum):
    Credit = "C"
    Debit = "D"
