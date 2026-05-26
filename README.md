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

# 📊 Metabase Dashboard — Climate & Extreme Weather Analytics

The project includes a fully interactive Metabase dashboard dedicated to climate analysis and extreme weather monitoring using Météo-France open datasets.

Dashboard name:

Climate & Extreme Weather Analytics Dashboard

The dashboard allows users to explore:

- temperature evolution;
- rainfall evolution;
- wind intensity;
- climate trends;
- weather station comparisons;
- geographic weather analysis;
- extreme weather events;
- weather condition distributions.

---

# 🎯 Dashboard Objectives

The dashboard was designed to:

- provide interactive climate analysis;
- visualize weather trends over time;
- highlight extreme weather conditions;
- compare weather stations;
- improve data storytelling using visual analytics;
- create a professional Business Intelligence interface with Metabase.

---

# 📈 Dashboard Visualizations

## KPI Cards

The dashboard includes several KPI indicators:

- Average Temperature
- Total Rainfall
- Maximum Wind Speed
- Average Temperature Risk Level

These KPIs provide a quick overview of the climate conditions.

---

# 🌡️ Climate Trends

Time-series visualizations include:

- Temperature Evolution Over Time
- Rainfall Evolution Over Time
- Climate Trends Over Time

These charts help identify:

- seasonal variations;
- rainfall peaks;
- climate fluctuations;
- long-term weather evolution.

---

# 🌦️ Advanced Weather Analysis

The dashboard contains advanced analytical visualizations:

## Heat vs Rainfall Correlation
Bubble chart showing the relationship between:

- temperature;
- rainfall;
- wind intensity.

## Weather Condition Distribution
Interactive donut chart representing:

- rainy days;
- hot days;
- windy days;
- normal weather conditions.

## Wind Intensity During Heatwaves
Analysis of wind intensity during high-temperature periods.

## Temperature Variability Analysis
Boxplot visualization showing:

- climate variability;
- outliers;
- temperature dispersion.

---

# 🗺️ Geographic Analysis

Geographic visualizations include:

- Regional Weather Station Map
- Top 10 Hottest Weather Stations
- Top 10 Rainiest Weather Stations
- 10 Strongest Wind Stations

The map visualization uses:

- latitude;
- longitude;
- station metadata from Météo-France datasets.

---

# 🚨 Extreme Weather Monitoring

The dashboard contains a dedicated section:

Extreme Weather Events

This table highlights:

- heatwaves;
- heavy rainfall;
- strong wind conditions;
- abnormal weather observations.

---

# 🎛️ Interactive Dashboard Filters

Several dynamic filters were implemented:

| Filter | Purpose |
|---|---|
| Date | Filter data by time period |
| Weather Station | Filter by station name |
| Temperature Filter | Filter by temperature values |

These filters dynamically update all connected visualizations in real time.

---

# 🧩 Dashboard Organization

The dashboard is structured into multiple sections:

1. KPI Overview
2. Climate Trends
3. Weather Analysis
4. Geographic & Station Analysis
5. Extreme Weather Events

This structure improves:

- readability;
- storytelling;
- dashboard navigation;
- user experience.

---

# 🎨 Data Visualization Approach

The dashboard uses multiple visualization types:

- line charts;
- bar charts;
- donut charts;
- bubble charts;
- boxplots;
- gauges;
- geographic maps;
- KPI cards;
- interactive tables.

This variety improves:

- analytical depth;
- storytelling;
- dashboard interactivity;
- visual clarity.

---

# 👩‍💻 Role — Data Visualization & Dashboard Development

This part of the project was responsible for:

- Metabase dashboard creation;
- KPI design;
- dashboard organization;
- interactive filters;
- weather storytelling;
- advanced visual analytics;
- geographic visualization;
- climate correlation analysis;
- dashboard UX/UI improvements.

---

# 🚀 Dashboard Access

Start Docker containers:

```bash
docker compose up -d
```

Open Metabase:

```text
http://localhost:3001
```

The dashboard is automatically available after startup thanks to the persisted Metabase configuration database:

```text
metabase-data/metabase.db.mv.db
```

---

# 📌 Final Result

The final dashboard provides:

- interactive climate monitoring;
- advanced weather analytics;
- dynamic filtering;
- professional Business Intelligence visualizations;
- data storytelling using Météo-France datasets.

The project fully satisfies the requirements of the Data Visualization course by combining:

- Docker;
- PostgreSQL;
- ETL pipeline;
- Metabase;
- OpenData weather datasets;
- interactive dashboards;
- geographic analytics;
- storytelling techniques.

# ▶️ How to Run the Project

## 1️⃣ Clone the repository

```bash
git clone <repository-url>
```

---

## 2️⃣ Go to the project folder

```bash
cd meteo-france-metabase-dashboard
```

---

## 3️⃣ Start Docker containers

```bash
docker compose up -d
```

---

## 4️⃣ Verify containers

```bash
docker ps
```

Expected containers:

- meteo_postgres
- meteo_metabase

---

# 🌐 Open Metabase

Open the following URL in your browser:

```text
http://localhost:3001
```

---

# 📊 Access the Dashboard

Inside Metabase, open:

```text
Climate & Extreme Weather Analytics Dashboard
```

The dashboard includes:

- KPI cards;
- climate trends;
- weather correlations;
- geographic maps;
- interactive filters;
- extreme weather analysis.

---

# 🎛️ Interactive Filters

The dashboard supports dynamic filtering:

- Date filter
- Weather Station filter
- Temperature filter

These filters update all connected visualizations in real time.

---

# 💾 Dashboard Persistence

The Metabase configuration database is persisted in:

```text
metabase-data/metabase.db.mv.db
```

This allows all dashboards, questions, visualizations, and filters to remain available after restarting Docker or cloning the repository.
