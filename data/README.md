# Data Directory

## Structure

```
data/
├── raw/          # Original source data
└── processed/    # Cleaned, merged output: produced by notebooks/01_data_cleaning.ipynb
```


## Raw Files

### worldbank.csv
| Field | Value |
|---|---|
| Source | World Bank|
| URL | https://data.worldbank.org |
| Collected by | `src/azdata/collect/worldbank.py` via `wbdata` Python package |
| Date collected | 2026-04-09 |
| Format | CSV |

**Indicators collected:**

| Column | WDI Code | Description |
|---|---|---|
| gdp | NY.GDP.MKTP.CD | Total GDP, current USD |
| gdp_growth | NY.GDP.MKTP.KD.ZG | Real GDP growth rate, annual % |
| inflation | FP.CPI.TOTL.ZG | Inflation, consumer prices, annual % |
| current_account | BN.CAB.XOKA.CD | Current account balance, USD |
| unemployment_rate | SL.UEM.TOTL.ZS | Unemployment rate, % of total labor force |
| exports_pct_gdp | NE.EXP.GNFS.ZS | Exports of goods and services, % of GDP |
| imports_pct_gdp | NE.IMP.GNFS.ZS | Imports of goods and services, % of GDP |


---

### fred.csv
| Field | Value |
|---|---|
| Source | Federal Reserve Bank of St. Louis |
| URL | https://fred.stlouisfed.org |
| Collected by | `src/azdata/collect/fred.py` via `fredapi` Python package |
| Date collected | 2026-04-09 |
| Format | CSV |

**Indicators collected:**

| Column | FRED Series | Description |
|---|---|---|
| oil_price | DCOILBRENTEU | Brent crude oil price, USD per barrel, aggregated to annual average |


---

### cbar_usd_azn.xlsx
| Field | Value |
|---|---|
| Source | Central Bank of the Republic of Azerbaijan (CBAR) |
| URL | https://cbar.az |
| Collected by | Manual download |
| Date collected | 2026-04-09 |
| Format | XLSX |


---

### statgov_gdp_split.xls
| Field | Value |
|---|---|
| Source | State Statistical Committee of the Republic of Azerbaijan |
| URL | https://stat.gov.az/source/system_nat_accounts/az/014.xls |
| Collected by | `src/azdata/collect/statgov.py` via direct file download |
| Date collected | 2026-04-09 |
| Format | XLS |


---

### statgov_wages.xls
| Field | Value |
|---|---|
| Source | State Statistical Committee of the Republic of Azerbaijan |
| URL | https://stat.gov.az/source/labour/az/004_2-3.xls |
| Collected by | `src/azdata/collect/statgov.py` via direct file download |
| Date collected | 2026-04-09 |
| Format | XLS |


---

### statgov_trade.xls
| Field | Value |
|---|---|
| Source | State Statistical Committee of the Republic of Azerbaijan |
| URL | https://stat.gov.az/source/trade/az/f_trade/xt001.xls |
| Collected by | `src/azdata/collect/statgov.py` via direct file download |
| Date collected | 2026-04-09 |
| Format | XLS |


---

### statgov_exports_structure.xls
| Field | Value |
|---|---|
| Source | State Statistical Committee of the Republic of Azerbaijan |
| URL | https://stat.gov.az/source/trade/az/f_trade/xt008_3.xls |
| Collected by | `src/azdata/collect/statgov.py` via direct file download |
| Date collected | 2026-04-09 |
| Format | XLS |


---

## Processed Files

### az_master.csv
| Field | Value |
|---|---|
| Produced by | `notebooks/01_data_cleaning.ipynb` |
| Year range | 2000–2024 |
| Index | Integer year |

**Columns:**

| Column | Source file | Description | Unit |
|---|---|---|---|
| year | — | Index | Integer |
| gdp_usd | worldbank.csv | Total GDP | Current USD |
| gdp_growth_pct | worldbank.csv | Real GDP growth rate | Annual % |
| inflation_pct | worldbank.csv | Consumer price inflation | Annual % |
| current_account_usd | worldbank.csv | Current account balance | USD |
| unemployment_pct | worldbank.csv | Unemployment rate | % of labor force |
| exports_pct_gdp | worldbank.csv | Exports of goods and services | % of GDP |
| imports_pct_gdp | worldbank.csv | Imports of goods and services | % of GDP |
| oil_price_usd | fred.csv | Brent crude oil price | Annual avg. USD/barrel |
| exchange_rate_azn | cbar_usd_azn.xlsx | USD/AZN official rate | Annual avg. AZN per USD |
| gdp_azn | statgov_gdp_split.xls | Total GDP at market prices | Million AZN |
| oil_gdp_azn | statgov_gdp_split.xls | Mining sector value added (oil proxy) | Million AZN |
| non_oil_gdp_azn | derived | Total GDP minus oil sector | Million AZN |
| oil_share_pct | derived | Oil GDP as % of total GDP | % |
| avg_wage_azn | statgov_wages.xls | Average monthly nominal wage | AZN |
| total_exports_usd | statgov_trade.xls | Total exports | Million USD |
| total_imports_usd | statgov_trade.xls | Total imports | Million USD |
| trade_balance_usd | statgov_trade.xls | Trade balance | Million USD |
| oil_exports_usd | statgov_exports_structure.xls | Oil and petroleum product exports | Million USD |
| non_oil_exports_usd | derived | Total exports minus oil exports | Million USD |
| non_oil_export_share_pct | derived | Non-oil exports as % of total exports | % |

**Known data gaps:**
- `oil_gdp_azn` and `non_oil_gdp_azn` unavailable before 2005. Rows 2000-2004 will be null for these columns.
- `avg_wage_azn`  unavailable before 2010, and only available for years 2010, 2015, 2020-2024. Rows outside these years will be null.
