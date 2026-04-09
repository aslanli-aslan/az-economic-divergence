# Azerbaijan Economic Divergence Dashboard

Azerbaijan has one of the most interesting economic development stories in the world. Built on oil wealth, the country spent decades with its GDP, exports, and government revenues almost entirely dependent on a single industry. This project examines whether that has actually changed — using data from five sources across GDP structure, inflation, labor markets, trade, and regional output.

**The central question: did Azerbaijan's economy genuinely diverge from oil over the past two decades, or is the non-oil growth just a number on paper?**

> Live dashboard: coming soon

---

## Data Sources

| Source | Link | Data Collected |
|---|---|---|
| World Bank WDI | [data.worldbank.org](https://data.worldbank.org) | GDP, inflation, unemployment, trade; 7 indicators |
| FRED - St. Louis Fed | [fred.stlouisfed.org](https://fred.stlouisfed.org) | CPI inflation, Brent oil price; 3 series |
| IMF World Economic Outlook | [imf.org](https://www.imf.org) | GDP growth, inflation, unemployment, debt; 6 indicators |
| Central Bank of Azerbaijan | [cbar.az](https://www.cbar.az) | USD/AZN official exchange rate |
| State Statistical Committee | [stat.gov.az](https://www.stat.gov.az) | Oil/non-oil GDP split, wages, trade balance, regional output |

---

## How to Run

Requires [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/aslanli-aslan/az-economic-divergence
cd az-economic-divergence
uv sync
```

To collect data:

```bash
uv run python src/azdata/collect/worldbank.py
uv run python src/azdata/collect/fred.py
```
