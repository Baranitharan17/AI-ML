import pandas as pd
import os

# #1.load the csv filed
# df=pd.read_csv("customers_raw.csv")

# #percentage of missing values per column
# print("% missing per column:")
# print((df.isna().mean()*100).round(2))
# #count duplicate rows
# print("\nNumber of Duplicate rows:")
# print(df.duplicated().sum())
# #count invalid ages below 0 or above 120
# invalid_ages=((df["age"]<0) | (df["age"]>120)).sum()
# print("\nNumber of invalid ages:")
# print(invalid_ages)
