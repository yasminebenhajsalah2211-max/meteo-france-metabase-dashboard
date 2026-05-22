import pandas as pd
from sqlalchemy import create_engine

CSV_PATH = "data/clean/clean_meteo.csv"

DB_USER = "meteo_user"
DB_PASSWORD = "meteo_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "meteo_db"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv(CSV_PATH)

df.to_sql(
    "meteo_daily",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into PostgreSQL successfully.")