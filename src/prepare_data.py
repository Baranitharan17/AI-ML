import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split

# Create reproducible synthetic support ticket dataset
categories = {
    "Account": [
        "Unable to login to my account",
        "I forgot my password",
        "Please help me reset my credentials",
        "My account is locked",
        "I cannot access my profile"
    ],
    "Billing": [
        "I was charged twice",
        "My invoice is incorrect",
        "Please refund my payment",
        "Payment failed but money was deducted",
        "I need my billing statement"
    ],
    "Technical": [
        "Application is crashing",
        "Website is not loading",
        "Software is running slowly",
        "I am facing a server error",
        "The application has a technical issue"
    ],
    "Delivery": [
        "My order has not arrived",
        "Package delivery is delayed",
        "I received the wrong product",
        "Please track my shipment",
        "My order is missing"
    ],
    "HR": [
        "What is the leave policy?",
        "How many casual leaves are available?",
        "I need my salary slip",
        "Please explain the attendance policy",
        "How can I apply for leave?"
    ],
    "General": [
        "What are the office timings?",
        "Where is the company office?",
        "I need general information",
        "Please contact me regarding my query",
        "I have a general question"
    ]
}

priorities = ["Low", "Medium", "High"]

records = []

for category, sentences in categories.items():
    for i in range(100):
        text = sentences[i % len(sentences)]
        priority = priorities[i % 3]

        records.append({
            "text": f"{text} - Ticket reference {category}-{i+1}",
            "category": category,
            "priority": priority
        })

df = pd.DataFrame(records)

# Create folders
Path("data/raw").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Save raw dataset
df.to_csv("data/raw/support_tickets.csv", index=False)

print("Original dataset shape:", df.shape)

# Clean text
df["text"] = df["text"].str.lower().str.strip()

# Remove duplicate rows
df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)

print("After cleaning:", df.shape)

# Check category balance
print("\nCategory balance:")
print(df["category"].value_counts())

# Check priority balance
print("\nPriority balance:")
print(df["priority"].value_counts())

# Joint stratification to preserve both labels
df["stratify_label"] = (
    df["category"] + "_" + df["priority"]
)

# 70% train, 30% temporary
train, temp = train_test_split(
    df,
    test_size=0.30,
    random_state=42,
    stratify=df["stratify_label"]
)

# Split remaining 30% into 15% validation and 15% test
validation, test = train_test_split(
    temp,
    test_size=0.50,
    random_state=42,
    stratify=temp["stratify_label"]
)

# Remove helper column
for dataset in [train, validation, test]:
    dataset.drop(columns=["stratify_label"], inplace=True)

# Save datasets
train.to_csv("data/processed/train.csv", index=False)
validation.to_csv("data/processed/validation.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)

print("\nDataset split:")
print("Train:", train.shape)
print("Validation:", validation.shape)
print("Test:", test.shape)

print("\nData preparation completed!")
