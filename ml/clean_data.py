import pandas as pd

INPUT_PATH = "ml/data/customer_churn.csv"
OUTPUT_PATH = "ml/data/customer_churn_cleaned.csv"

# Load dataset
df = pd.read_csv(INPUT_PATH)

print("Original shape:", df.shape)

# 1. Remove unnecessary ID column
df.drop("customerID", axis=1, inplace=True)

# 2. Convert blank strings to NaN
df.replace(" ", pd.NA, inplace=True)

# 3. Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# 4. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 5. Remove rows containing missing values
df.dropna(inplace=True)

# 6. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 7. Convert target variable
df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

print("\nCleaned shape:", df.shape)

print("\nFinal data types:")
print(df.dtypes)

print("\nFinal churn distribution:")
print(df["Churn"].value_counts())

# Save cleaned dataset
df.to_csv(OUTPUT_PATH, index=False)

print(f"\nCleaned dataset saved to: {OUTPUT_PATH}")