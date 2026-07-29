# automobile_recession

Exploratory data analysis of U.S. automobile sales, using `matplotlib` and `seaborn` to visualize how sales trends behave during recession periods versus non-recession periods.

## Data

`automobile_sales.csv` (sourced from IBM Skills Network Labs) contains monthly observations from 1980-2023, including automobile sales, GDP, unemployment rate, consumer confidence, seasonality weight, vehicle price, advertising expenditure, competition, and vehicle type (Superminicar, Smallfamilycar, Mediumfamilycar, Executivecar, Sports).

Recession periods covered:

- 1980
- 1981-1982
- 1991
- 2000-2001
- late 2007-mid 2009
- Feb-Apr 2020

## Analysis

The notebook (`automobile_jupyter.ipynb`) works through the following questions:

1. How does average automobile sales fluctuate year to year?
2. How does advertising expenditure correlate with sales during non-recession periods?
3. How do sales trends per vehicle type differ between recession and non-recession periods?
4. How did GDP vary over time during recession vs. non-recession periods?
5. How has seasonality (month of year) impacted sales?
6. What is the relationship between consumer confidence and sales during recessions?
7. How did advertising expenditure change during recession vs. non-recession periods?
8. What's the breakdown of advertising expenditure by vehicle type during recessions?
9. What effect does unemployment rate have on sales by vehicle type during recessions?

## Dashboard

`automobile_dashboard.py` is an interactive [Dash](https://dash.plotly.com/) app that turns the same dataset into a browsable report. Run it with:

```bash
python automobile_dashboard.py
```

then open the local URL it prints (default `http://127.0.0.1:8050`).

A dropdown lets you switch between two report types:

- **Recession Period Statistics** — four charts covering average sales by year, average sales by vehicle type, advertising expenditure share by vehicle type, and the effect of unemployment rate on sales by vehicle type, all restricted to recession periods.
- **Yearly Statistics** — pick a year from the second dropdown (enabled only for this report type) to see total yearly sales, total monthly sales, average sales by vehicle type, and advertising expenditure share by vehicle type, for that year.

## Key findings

- Overall automobile sales drop noticeably during recession periods, most visibly in the 2000-2001 and 2007-2009 downturns.
- Supermini cars sell relatively well during recessions, while small family cars lead during non-recession periods; executive and sports cars are hit hardest by recessions.
- GDP is lower and more volatile during recessions.
- December sees the highest seasonal sales; August the lowest.
- Consumer confidence shows little to no linear correlation with sales during recessions (r ≈ 0.05).
- Vehicle price is only weakly correlated with sales (r ≈ -0.17 in recessions, -0.06 otherwise).
- Advertising spend is heavily skewed toward non-recession periods (82.7% vs. 17.3%), and during recessions is spent mostly on small family cars.
- Sales trend downward as unemployment rises, across nearly all vehicle types.
