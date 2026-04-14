import os

from dotenv import load_dotenv
from fredapi import Fred

from azdata.paths import RAW_DIR

load_dotenv()


FRED_API_KEY = os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)


# Oil Price
oil_price = fred.get_series('DCOILBRENTEU', frequency="a", aggregation_method="avg")


# Join and save
oil_price.name = "oil_price"
oil_price.index.name = "year"
oil_price.to_csv(RAW_DIR / "fred.csv")
