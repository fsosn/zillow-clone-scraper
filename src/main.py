from scraper import scrape
from export import export_to_xlsx
from constants import URL


def main():
    df = scrape(URL)
    export_to_xlsx(df)


if __name__ == "__main__":
    main()
