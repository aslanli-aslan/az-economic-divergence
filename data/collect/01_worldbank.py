import wbdata
import pandas as pd

from azdata.paths import RAW_DIR


# Total GDP (Current USD)
total_gdp = wbdata.get_dataframe({'NY.GDP.MKTP.CD': 'gdp'}, country='AZ')


# GDP Growth Rate (Annual)
gdp_growth = wbdata.get_dataframe({'NY.GDP.MKTP.KD.ZG': 'gdp_growth'}, country='AZ')


# Inflation
inflation = wbdata.get_dataframe({'FP.CPI.TOTL.ZG': 'inflation'}, country='AZ')


# Current Account Balance
current_account = wbdata.get_dataframe({'BN.CAB.XOKA.CD': 'current_account'}, country='AZ')


# Unemployment Rate
unemployment_rate = wbdata.get_dataframe({'SL.UEM.TOTL.ZS': 'unemployment_rate'}, country='AZ')


# Exports % of GDP
exports_pct_gdp = wbdata.get_dataframe({'NE.EXP.GNFS.ZS': 'exports_pct_gdp'}, country='AZ')


# Imports % of GDP
imports_pct_gdp = wbdata.get_dataframe({'NE.IMP.GNFS.ZS': 'imports_pct_gdp'}, country='AZ')


# Join and save
worldbank = pd.concat([total_gdp, unemployment_rate, exports_pct_gdp,gdp_growth, inflation, current_account, imports_pct_gdp], axis=1)
worldbank.index.name = 'year'
worldbank = worldbank.sort_index()
worldbank.to_csv(RAW_DIR / 'worldbank.csv')