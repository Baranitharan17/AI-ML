import pandas as pd

#load raw data
df=pd.read_csv("customers_raw.csv")
#print("Column names:")
#print(df.columns.tolist())
#clean the column names
df.columns=df.columns.str.strip().str.lower()
#trim spaces and standardize text
for col in ["customer_name","email","city","phone"]:
    df[col]=df[col].astype("string").str.strip()
    df[col]=df[col].replace("",pd.NA)
df["customer_name"]=df["customer_name"].str.title()
df["email"]=df["email"].str.lower()
df["city"]=df["city"].str.title()
#standardize age and phone data
df["age"]=pd.to_numeric(df["age"],errors="coerce")
df["phone"]=df["phone"].astype("string")
#flag invalid values before removing duplicates
df["invalid_age"]=(df["age"]<0) | (df["age"]>120)
df["missing_email"]=df["email"].isna()
df["invalid_email"]=(
    df["email"].notna()
    & ~df["email"].str.match(
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$", na=False
    )
)
df["invalid_phone"]=(
    df["phone"].notna()
    & ~df["phone"].str.fullmatch(r"\d{10}",na=False)
)
#flag possible duplicate customers
df["possible_duplicate"]=(
    df.duplicated(subset=["email"],keep=False)
    & df["email"].notna()
)|(
    df.duplicated(subset=["customer_name","phone"],keep=False)
    & df["customer_name"].notna()
    & df["phone"].notna()
)
#remove exact duplicate rows
before=len(df)
df=df.drop_duplicates()
removed=before-len(df)

#save cleaned data with quality flags
df.to_csv("customers_cleaned.csv", index=False)

#print summary
print("Original rows:", before)
print("Exact duplicate rows removed:", removed)
print("Rows remaining:", len(df))
print("Invalid ages:",df["invalid_age"].sum())
print("Missing emails:",df["missing_email"].sum())
print("Invalid emails:",df["invalid_email"].sum())
print("Invalid phones:",df["invalid_phone"].sum())
print("Possible duplicate customers:",df["possible_duplicate"].sum())
print("\nCleaned data saved to customers_cleaned.csv")