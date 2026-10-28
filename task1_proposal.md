Technical Proposal: Predict Late Invoice Payment

1. Problem

Businesses often face cash-flow problems when customers pay invoices after the due date. Manually tracking every invoice makes it difficult to identify late payments in advance. The goal is to predict which invoices are likely to be paid late so the finance team can send reminders, follow up with customers, and improve cash-flow planning.

2. Recommended Approach

Use a supervised Machine Learning model trained on historical invoice data. Start with Random Forest as a baseline and compare it with XGBoost, which can capture more complex patterns in structured data.

Required features include:

- Customer payment history: Previous late payments, average payment delay, and percentage of invoices paid late.
- Invoice details: Invoice amount, invoice date, and due date.
- Payment terms: Number of credit days and agreed payment conditions.
- Additional useful features: Customer tenure, outstanding balance, and number of open invoices.

The target label is "1" if an invoice was paid after its due date and "0" if it was paid on or before the due date. Only information available at prediction time should be used to avoid data leakage.

3. Data Requirements

Request at least 5,000 historical invoice records with labelled payment outcomes, covering both late and on-time payments. Ideally, obtain 12–24 months of history and enough examples of late payments to represent different customer types.

Before modelling, check for missing values, duplicate invoice IDs, invalid dates, inconsistent payment terms, incorrect amounts, and inconsistent late-payment labels. Verify that paid invoices have payment dates and that the due date is reliable. Keep unpaid invoices separate unless their due dates have passed and their status can be labelled appropriately. Split training and testing data by time to simulate future predictions.

4. Evaluation Metric

Evaluate the model on a separate, later-period test dataset.

- Primary metric: ROC-AUC target of at least 0.80, measuring how well the model ranks late invoices above on-time invoices.
- Precision target: At least 70%, so most invoices flagged as high risk are genuinely late.
- Recall target: At least 75%, so the model identifies a useful proportion of late invoices.

Accuracy alone can be misleading because on-time payments may be much more common than late payments. A model that predicts every invoice as on time could achieve high accuracy while failing to identify late payments. Precision and recall help measure the usefulness of risk alerts. These targets should be validated against the actual dataset.

5. Estimated Build Time

Estimated duration: 10–12 working days, assuming the required data is accessible.

- Days 1–2: Understand business requirements and inspect data quality.
- Days 3–4: Clean data, engineer features, and define labels.
- Days 5–7: Train Random Forest and XGBoost models.
- Days 8–9: Evaluate metrics, tune the model, and analyse errors.
- Days 10–12: Build a risk-score prototype, validate with the finance team, and document results.

Production deployment and integration with accounting systems may require additional time.

6. Key Trade-offs

A simple rule such as “flag customers who were late twice before” is easy to explain, quick to implement, and requires little training data. However, it ignores invoice amount, payment terms, and changing customer behaviour, potentially missing new risks.

An ML model combines multiple signals and can rank invoices by predicted risk, enabling more targeted follow-ups. However, it needs reliable historical data, ongoing monitoring, and more development effort. Recommend starting with a simple rule as a baseline, then using Random Forest or XGBoost if data quality and predictive performance justify the additional complexity. Use risk scores to support finance-team decisions rather than automatically penalising customers.