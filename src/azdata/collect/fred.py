import os

import pandas as pd
from dotenv import load_dotenv
from fredapi import Fred

from azdata.paths import RAW_DIR

load_dotenv()


FRED_API_KEY = os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)


# Oil Price
oil_price = fred.get_series('DCOILBRENTEU', frequency="a", aggregation_method="avg")


# Join and save
fred_ = pd.concat([oil_price], axis=1, sort=True)
fred_.columns = ["inflation_cpi", "inflation_cpi_imf", "oil_price"]
fred_.index.name = "year"
fred_.to_csv(RAW_DIR / "fred.csv")
