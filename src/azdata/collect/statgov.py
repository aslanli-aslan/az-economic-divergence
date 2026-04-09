import requests

from azdata.paths import RAW_DIR


def download(url, filename):
    response = requests.get(url) 

    if response.status_code == 200:
        with open(RAW_DIR / filename, "wb") as f:
            f.write(response.content)


# Exports Structure
download('https://stat.gov.az/source/trade/az/f_trade/xt008_3.xls', 'statgov_exports_structure.xls')

#  Foreign Trades
download('https://stat.gov.az/source/trade/az/f_trade/xt001.xls', 'statgov_trade.xls')

# GDP Split Across Fields
download('https://stat.gov.az/source/system_nat_accounts/az/014.xls', 'statgov_gdp_split.xls')

# Average wages
download('https://stat.gov.az/source/labour/az/004_2-3.xls', 'statgov_wages.xls')
