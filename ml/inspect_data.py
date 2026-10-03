import pandas as pd

DATA_PATH = "ml/data/customer_churn.csv"

df = pd.read_csv(DATA_PATH)

print("Shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nTarget distribution:")
print(df["Churn"].value_counts())

print("\nTarget percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)