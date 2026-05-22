import pandas as pd
import os

INPUT_PATH = "data/raw/Q_01_previous-1950-2024_RR-T-Vent.csv"
OUTPUT_PATH = "data/clean/clean_meteo.csv"

os.makedirs("data/clean", exist_ok=True)

df = pd.read_csv(INPUT_PATH, sep=";", low_memory=False)

# nettoyer noms colonnes
df.columns = df.columns.str.lower().str.strip()

print("Columns:")
print(df.columns)

# garder colonnes utiles
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

available_columns = [col for col in columns_to_keep if col in df.columns]

df = df[available_columns]

# supprimer doublons
df = df.drop_duplicates()

# convertir date
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# supprimer lignes vides
df = df.dropna(how="all")

# sauvegarde
df.to_csv(OUTPUT_PATH, index=False)

print("Clean dataset saved.")
print(df.head())