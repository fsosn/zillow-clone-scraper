import re
import pandas as pd


def clean_dataframe(df: pd.DataFrame):
    df["price"] = df["price"].apply(_clean_price)
    df["address"] = df["address"].apply(_clean_address)
    return df


def _clean_price(price):
    match = re.search(r"\$?(\d+,\d+|\d+)", price)
    return int(match.group(1).replace(",", ""))


def _clean_address(address):
    address = re.sub(r"\s*\|\s*", " ", address)
    address = re.sub(r"\s+", " ", address)
    address = address.strip()
    return address
