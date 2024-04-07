from typing import Literal
from pandas import DataFrame
import pandas


def process_csv(row: ndarray, dateFormat: dict[Literal['dayfirst', 'yearfirst'], bool]) -> DataFrame:
    df2 = pandas.DataFrame()
    df2["maple_txn_date"] = pandas.to_datetime(
        row[data.txn_date_field], dayfirst=dateFormat["dayfirst"], yearfirst=dateFormat["yearfirst"]
    ).dt.date
    df.fillna(value="", inplace=True)
    return df2