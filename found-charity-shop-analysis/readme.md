# Found Charity Shop — Sales & Customer Insights (2024–2025)

A self-directed data analytics project built from real till data volunteered to me by a
local charity shop, turned into a set of business insights and presented back to the
shop manager as a slide deck.

## Project summary

The shop had two years of daily till exports (sales, guest counts, units sold, and a
14-category sales breakdown) but no way to turn that into decisions. I cleaned the data,
built three models to answer different questions, and delivered the findings as a
non-technical presentation.

| Question | Method used |
|---|---|
| Which single factor best predicts a day's takings? | Multiple linear regression (OLS, `statsmodels`) |
| Is there a seasonal pattern, and where's the business heading? | Time-series decomposition & forecasting (`Prophet`) |
| Do different months naturally fall into distinct "types"? | Unsupervised clustering (`KMeans`, `scikit-learn`) |
| Which categories and time periods matter most? | Exploratory analysis & a category × month heatmap (`pandas`, `seaborn`) |



