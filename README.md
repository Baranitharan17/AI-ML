<<<<<<< HEAD

# Support Ticket Classification

## Project Overview
This project prepares a dataset for classifying customer support tickets based on category and priority.

## Dataset Description
- Total records: 600
- Columns: text, category, priority
- Categories: Account, Billing, Technical, Delivery, HR, General
- Priorities: Low, Medium, High

## Dataset Source
This is a synthetically generated dataset created using Python.
It contains 600 sample support tickets based on common
customer support scenarios.

No real customer information is used.

## Data Cleaning
1. Converted ticket text to lowercase.
2. Removed leading and trailing spaces.
3. Removed duplicate ticket records.
4. Checked category class balance.
5. Checked priority class balance.

## Dataset Split
- Training: 70% (420 records)
- Validation: 15% (90 records)
- Testing: 15% (90 records)

Stratified splitting was performed using the
combined category and priority labels.

## Folder Structure
- data/raw: Original dataset
- data/processed: Cleaned train, validation and test datasets
- src: Data preparation Python script
- notebooks: Jupyter notebook

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

## Execution
Run the following command:

python src/prepare_data.py

## Output
Three datasets are generated:
- train.csv
- validation.csv
- test.csv
=======
# AI-ML
>>>>>>> 31461921fdc4cf9459c818e7408334cec0310984
