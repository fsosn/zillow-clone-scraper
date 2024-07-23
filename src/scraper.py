from bs4 import BeautifulSoup
import requests
import pandas as pd
from typing import Any
from clean_data import clean_dataframe


def scrape(url: str) -> pd.DataFrame:
    page_content = _fetch_page(url)
    soup = BeautifulSoup(page_content, "lxml")
    articles = soup.find_all("article")
    estate_details_dict_list = [_get_estate_details(article) for article in articles]
    raw_df = pd.DataFrame(estate_details_dict_list)
    return clean_dataframe(raw_df)


def _fetch_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def _get_estate_details(article: Any) -> dict[str, Any]:
    href = article.find("a").get("href")
    price = article.find("span").get_text(strip=True)
    address = article.find("address").get_text(strip=True)
    return {"price": price, "address": address, "link": href}
