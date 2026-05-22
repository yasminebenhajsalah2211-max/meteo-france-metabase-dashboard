# 🌦️ Météo France x Metabase Dashboard

## 📌 Project Overview

This project is an interactive weather dashboard built using open data from Météo-France.

The objective is to analyze weather conditions in France using historical climatological datasets and visualize the results through interactive dashboards created with Metabase.

The project focuses on:

- temperature analysis;
- rainfall analysis;
- wind analysis;
- geographic visualization of weather stations;
- data storytelling with interactive dashboards.

---

# 🛠️ Technical Stack

| Tool | Usage |
|---|---|
| Python | Data preprocessing and ETL |
| PostgreSQL | Weather data storage |
| Docker | Containerization |
| Metabase | Interactive dashboard |
| CSV | Raw Météo-France datasets |
| GeoJSON | Geographic visualization |

---

# 🏗️ Technical Architecture

```text
Météo-France CSV
        ↓
Python ETL Scripts
        ↓
PostgreSQL Database
        ↓
Metabase
        ↓
Interactive Dashboard
```

---

# 📁 Repository Structure

```text
meteo-france-metabase/
├── data/
│   ├── raw/
│   └── clean/
├── notebooks/
│   └── exploration.ipynb
├── scripts/
│   ├── extract_data.py
│   ├── clean_data.py
│   └── load_to_postgres.py
├── dashboard/
│   └── geojson/
│       ├── regions.geojson
│       └── departements.geojson
├── presentation/
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

# 📊 Data Sources

## Main Dataset

Daily climatological data from Météo-France OpenData:

- minimum / maximum / average temperatures;
- rainfall;
- wind measurements;
- weather station information.

Source:

```text
https://meteo.data.gouv.fr/
```

---

## GeoJSON Files

Used for map visualizations in Metabase:

### Regions

```text
https://france-geojson.gregoiredavid.fr/repo/regions.geojson
```

### Departments

```text
https://france-geojson.gregoiredavid.fr/repo/departements.geojson
```

---

# 🐳 Docker Setup

The project uses Docker Compose with:

- PostgreSQL;
- Metabase.

## Start containers

```bash
docker compose up -d
```

## Verify containers

```bash
docker ps
```

Expected containers:

```text
meteo_postgres
meteo_metabase
```

---

# 🌐 Metabase Access

Open Metabase:

```text
http://localhost:3001
```

---

# 🗄️ PostgreSQL Configuration

Database connection used in Metabase:

| Parameter | Value |
|---|---|
| Host | postgres |
| Port | 5432 |
| Database | meteo_db |
| Username | meteo_user |
| Password | meteo_password |

⚠️ Important:

Inside Metabase, the host is:

```text
postgres
```

NOT:

```text
localhost
```

---

# ⚙️ ETL Pipeline

The project follows an ETL workflow:

```text
Extract → Clean → Load
```

---

## 1️⃣ Extract

```bash
python scripts/extract_data.py
```

Handles data extraction.

---

## 2️⃣ Clean

```bash
python scripts/clean_data.py
```

Cleaning operations include:

- selecting useful columns;
- removing duplicates;
- converting dates;
- converting numeric values;
- handling missing values.

### Missing values strategy

| Data Type | Strategy |
|---|---|
| Temperature columns | Mean imputation |
| Rainfall and wind columns | Median imputation |

---

## 3️⃣ Load

```bash
python scripts/load_to_postgres.py
```

Loads cleaned data into PostgreSQL.

Final table:

```text
meteo_daily
```

---

# 🧹 Cleaned Dataset Columns

```text
num_poste
nom_usuel
lat
lon
alti
aaaammjj
rr
tn
tx
tm
ffm
fxy
```

---

# 📈 Exploratory Notebook

The notebook:

```text
notebooks/exploration.ipynb
```

contains:

- dataset exploration;
- statistics;
- missing values analysis;
- temperature distribution visualization.

---

# 🚫 Large Files

Raw CSV files are not pushed to GitHub because they exceed GitHub's file size limit (100 MB).

Ignored folders:

```text
data/raw/
data/clean/
venv/
```

---

# 🔀 Git Workflow

Development branch used:

```text
yasmine-setup
```

Useful commands:

```bash
git add scripts/
git add README.md
git add docker-compose.yml
git add notebooks/

git commit -m "Finalize data engineering pipeline"

git push
```

---

# 👩‍💻 Role — Data Engineer

This part of the project was responsible for:

- GitHub repository setup;
- Docker configuration;
- PostgreSQL setup;
- Metabase connection;
- ETL pipeline development;
- dataset cleaning;
- PostgreSQL table creation;
- project documentation.

---

# 🚀 Next Steps

The dashboard team can now:

- create visualizations in Metabase;
- build dashboards;
- add filters;
- import GeoJSON maps;
- prepare the final presentation.