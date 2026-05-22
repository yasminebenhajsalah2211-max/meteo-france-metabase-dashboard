import pandas as pd
import os

INPUT_PATH = "data/raw/Q_01_previous-1950-2024_RR-T-Vent.csv"
OUTPUT_PATH = "data/clean/clean_meteo.csv"

os.makedirs("data/clean", exist_ok=True)

# Load dataset
df = pd.read_csv(INPUT_PATH, sep=";", low_memory=False)

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Keep useful columns
columns_to_keep = [
    "num_poste",
    "nom_usuel",
    "lat",
    "lon",
    "alti",
    "aaaammjj",
    "rr",
    "tn",
    "tx",
    "tm",
    "ffm",
    "fxy"
]

df = df[columns_to_keep]

# Convert numeric columns
numeric_cols = [
    "rr",
    "tn",
    "tx",
    "tm",
    "ffm",
    "fxy"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Replace missing values

# Temperatures -> mean
temp_cols = ["tn", "tx", "tm"]

for col in temp_cols:
    df[col] = df[col].fillna(df[col].mean())

# Rain/Wind -> median
other_cols = ["rr", "ffm", "fxy"]

for col in other_cols:
    df[col] = df[col].fillna(df[col].median())

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["aaaammjj"] = pd.to_datetime(
    df["aaaammjj"],
    format="%Y%m%d",
    errors="coerce"
)

# Remove rows with invalid dates
df = df.dropna(subset=["aaaammjj"])

# Save clean dataset
df.to_csv(OUTPUT_PATH, index=False)

print("Clean dataset saved successfully.")
print(df.head())

# Check remaining missing values
print("\nMissing values:")
print(df.isnull().sum())