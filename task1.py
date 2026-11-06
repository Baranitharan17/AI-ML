import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix
)
from sklearn.cluster import KMeans


# 1. Create raw support-ticket data
data = [
    ("I was charged twice for my subscription", "billing"),
    ("Please explain my latest invoice", "billing"),
    ("Refund has not reached my bank account", "billing"),
    ("My payment failed but money was deducted", "billing"),
    ("How can I update my billing address", "billing"),
    ("I need a copy of my invoice", "billing"),
    ("Why is my subscription price higher", "billing"),
    ("Cancel the extra charge on my account", "billing"),
    ("Payment receipt is missing", "billing"),
    ("I was charged twice for my subscription", "billing"),

    ("The application crashes when I open it", "technical"),
    ("I cannot connect to the company VPN", "technical"),
    ("The website shows a server error", "technical"),
    ("My laptop software is not responding", "technical"),
    ("Email is not syncing on my phone", "technical"),
    ("The application crashes when I open it", "technical"),
    ("I cannot upload my document", "technical"),
    ("Printer is not connecting to my computer", "technical"),
    ("The dashboard loads very slowly", "technical"),
    ("I receive an error while logging in", "technical"),

    ("I forgot my password", "account"),
    ("Please unlock my account", "account"),
    ("How do I change my username", "account"),
    ("I need to update my profile details", "account"),
    ("My account has been locked", "account"),
    ("I forgot my password", "account"),
    ("How can I reset my login credentials", "account"),
    ("Please deactivate my old account", "account"),
    ("I cannot verify my email address", "account"),
    ("I want to change my registered email", "account"),

    ("Where can I find my tax invoice", "BILLING"),
    ("PAYMENT WAS DEDUCTED TWICE", "BILLING"),
    ("software installation failed", "TECHNICAL"),
    ("NETWORK CONNECTION IS NOT WORKING", "TECHNICAL"),
    ("ACCOUNT PASSWORD RESET REQUEST", "ACCOUNT"),
    ("my profile details are incorrect", "ACCOUNT"),
    ("Need help with my monthly payment", "billing"),
    ("Application is showing a blank screen", "technical"),
    ("Please recover my account access", "account"),
    ("How do I update payment information", "billing"),
    ("The system stopped working today", "technical"),
    ("I cannot access my user profile", "account"),
    ("", "billing"),
    ("My invoice amount looks incorrect", None),
    (None, "technical"),
    ("Unable to update payment details", "billing"),
    ("", None),
    ("Account access is not working", "account"),
]

df = pd.DataFrame(data, columns=["text", "category"])

# Add inconsistent casing
df.loc[df.index % 7 == 0, "text"] = (
    df.loc[df.index % 7 == 0, "text"].astype("string").str.upper()
)

# Save raw dataset
df.to_csv("tickets_raw.csv", index=False)


# 2. Audit function
def audit(dataframe):
    return {
        "rows": len(dataframe),
        "missing_text": int(dataframe["text"].isna().sum()),
        "missing_category": int(dataframe["category"].isna().sum()),
        "missing_cells_percent": round(
            dataframe.isna().sum().sum()
            / dataframe.size * 100, 2
        ),
        "duplicate_rows": int(dataframe.duplicated().sum()),
        "category_balance": dataframe["category"].value_counts(
            dropna=False
        ).to_dict()
    }


before = audit(df)

print("\nBEFORE CLEANING")
print(before)


# 3. Clean data
clean = df.copy()

clean["text"] = clean["text"].astype("string").str.strip()
clean["category"] = (
    clean["category"].astype("string").str.strip().str.lower()
)

# Treat blank text as missing
clean["text"] = clean["text"].replace("", pd.NA)

# Remove rows with missing text or category
clean = clean.dropna(subset=["text", "category"])

# Remove duplicate rows
clean = clean.drop_duplicates()

# Keep only the requested categories
valid_categories = ["billing", "technical", "account"]
clean = clean[clean["category"].isin(valid_categories)].copy()

clean["text"] = clean["text"].str.lower()

clean.to_csv("tickets_clean.csv", index=False)

after = audit(clean)

print("\nAFTER CLEANING")
print(after)

print("\nBEFORE / AFTER SUMMARY")
print(f"Rows: {before['rows']} -> {after['rows']}")
print(
    f"Missing cells (%): "
    f"{before['missing_cells_percent']} -> "
    f"{after['missing_cells_percent']}"
)
print(
    f"Duplicate rows: "
    f"{before['duplicate_rows']} -> "
    f"{after['duplicate_rows']}"
)
print("Category balance before:", before["category_balance"])
print("Category balance after:", after["category_balance"])


# 4. Prepare an 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(
    clean["text"],
    clean["category"],
    test_size=0.20,
    random_state=42,
    stratify=clean["category"]
)

# Fit TF-IDF on training data only
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

labels = ["account", "billing", "technical"]


# 5. Baseline: always predict the most common training category
majority_category = y_train.value_counts().idxmax()

baseline_predictions = np.repeat(
    majority_category, len(y_test)
)


# 6. TF-IDF + Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)


# 7. Evaluate both models
def evaluate(name, actual, predicted):
    accuracy = accuracy_score(actual, predicted)
    macro_f1 = f1_score(
        actual, predicted,
        labels=labels,
        average="macro",
        zero_division=0
    )
    matrix = confusion_matrix(
        actual, predicted, labels=labels
    )

    print(f"\n{name}")
    print("Accuracy:", round(accuracy, 4))
    print("Macro F1:", round(macro_f1, 4))
    print("Confusion matrix (rows=actual, columns=predicted)")
    print(pd.DataFrame(
        matrix,
        index=labels,
        columns=labels
    ))

    return accuracy, macro_f1, matrix


baseline_metrics = evaluate(
    "BASELINE MODEL",
    y_test, baseline_predictions
)

model_metrics = evaluate(
    "TF-IDF + LOGISTIC REGRESSION",
    y_test, predictions
)


# 8. List three misclassified tickets
results = pd.DataFrame({
    "text": X_test.to_numpy(),
    "actual": y_test.to_numpy(),
    "predicted": predictions
})

wrong = results[results["actual"] != results["predicted"]].copy()

def reason(row):
    if "payment" in row["text"] or "invoice" in row["text"]:
        return "Payment/invoice wording may overlap with other categories."
    if "login" in row["text"] or "access" in row["text"]:
        return "Login/access wording may overlap between account and technical."
    return "Short or ambiguous wording provides limited category context."

wrong["reason"] = wrong.apply(reason, axis=1)

print("\nTHREE MISCLASSIFIED TICKETS")
if len(wrong) > 0:
    print(wrong.head(3).to_string(index=False))
else:
    print("No misclassified tickets in this test split.")


# 9. KMeans on the same TF-IDF feature space, without labels
# Use all cleaned text; category labels are not passed to KMeans.
all_tfidf = vectorizer.fit_transform(clean["text"])

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

cluster_ids = kmeans.fit_predict(all_tfidf)

cluster_results = clean.copy()
cluster_results["cluster"] = cluster_ids

comparison = pd.crosstab(
    cluster_results["cluster"],
    cluster_results["category"]
)

print("\nKMEANS CLUSTERS VS REAL CATEGORIES")
print(comparison)

print("\nTHREE-LINE CLUSTER COMPARISON")
for cluster_id in sorted(cluster_results["cluster"].unique()):
    subset = cluster_results[
        cluster_results["cluster"] == cluster_id
    ]
    counts = subset["category"].value_counts()
    dominant = counts.idxmax()
    purity = counts.max() / len(subset)

    print(
        f"Cluster {cluster_id}: {len(subset)} tickets; "
        f"most common category = {dominant}; "
        f"dominant-category share = {purity:.1%}."
    )


# 10. Save report
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("DATA AUDIT AND MODEL EVALUATION\n\n")
    report.write(f"Before cleaning: {before}\n\n")
    report.write(f"After cleaning: {after}\n\n")
    report.write(f"Baseline accuracy: {baseline_metrics[0]:.4f}\n")
    report.write(f"Baseline macro F1: {baseline_metrics[1]:.4f}\n")
    report.write(f"Baseline confusion matrix:\n{baseline_metrics[2]}\n\n")
    report.write(f"Model accuracy: {model_metrics[0]:.4f}\n")
    report.write(f"Model macro F1: {model_metrics[1]:.4f}\n")
    report.write(f"Model confusion matrix:\n{model_metrics[2]}\n\n")
    report.write("Misclassified tickets:\n")
    report.write(
        wrong.head(3).to_string(index=False)
        if len(wrong) else "No errors in this test split."
    )
    report.write("\n\nKMeans comparison:\n")
    report.write(comparison.to_string())

print("\nCreated: tickets_raw.csv, tickets_clean.csv, report.txt")
