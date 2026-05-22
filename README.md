Météo France × Metabase Dashboard

Tableau de bord météo interactif basé sur les données ouvertes de Météo-France, stockées dans PostgreSQL et visualisées via Metabase.


Table des matières

Aperçu du projet
Stack technique
Architecture
Structure du dépôt
Sources de données
Lancer le projet
Pipeline ETL
Colonnes du dataset nettoyé
Connexion Metabase → PostgreSQL
Notes sur les fichiers de données
Workflow Git
Rôle : Data Engineer
Prochaines étapes


Aperçu du projet
Ce projet est un tableau de bord météo interactif construit à partir des données ouvertes de Météo-France.
L'objectif est d'analyser les conditions météorologiques en France à partir de données climatologiques historiques, puis de visualiser les résultats dans un dashboard Metabase interactif.
Le projet couvre :

l'analyse des températures
l'analyse des précipitations
l'analyse du vent
la visualisation géographique des stations météo
le data storytelling via des dashboards interactifs


Stack technique
OutilUsagePythonPrétraitement et ETLPostgreSQLStockage des donnéesDockerConteneurisationMetabaseCréation des dashboardsCSV Météo-FranceSource de données brutesGeoJSONRégions et départements français

Architecture
Météo-France CSV
       ↓
Scripts ETL Python
       ↓
Base de données PostgreSQL
       ↓
Metabase
       ↓
Dashboard interactif

Structure du dépôt
meteo-france-metabase/
├── data/
│   ├── raw/                    # Données brutes (non versionnées)
│   └── clean/                  # Données nettoyées (non versionnées)
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

Sources de données
Dataset principal
Données climatologiques journalières issues de Météo-France OpenData :

températures (min, max, moyenne)
précipitations
vent
informations sur les stations météo

Source : https://meteo.data.gouv.fr/
Fichiers GeoJSON
Utilisés pour les visualisations géographiques dans Metabase :

Régions : https://france-geojson.gregoiredavid.fr/repo/regions.geojson
Départements : https://france-geojson.gregoiredavid.fr/repo/departements.geojson


Lancer le projet
1. Démarrer les conteneurs Docker
bashdocker compose up -d
2. Vérifier les conteneurs actifs
bashdocker ps
Conteneurs attendus : meteo_postgres et meteo_metabase
3. Ouvrir Metabase
http://localhost:3001

Pipeline ETL
Le pipeline suit trois étapes : Extract → Clean → Load
1. Extract
bashpython scripts/extract_data.py
2. Clean
bashpython scripts/clean_data.py
Opérations effectuées :

sélection des colonnes utiles
renommage des colonnes
conversion des valeurs numériques et des dates
suppression des doublons
gestion des valeurs manquantes :

colonnes de température → remplissage par la moyenne
colonnes de précipitations et de vent → remplissage par la médiane



3. Load
bashpython scripts/load_to_postgres.py
Table PostgreSQL finale : meteo_daily

Colonnes du dataset nettoyé
ColonneDescriptionnum_posteIdentifiant de la station météonom_usuelNom de la station météolatLatitudelonLongitudealtiAltitudeaaaammjjDaterrPrécipitationstnTempérature minimaletxTempérature maximaletmTempérature moyenneffmVitesse moyenne du ventfxyRafale de vent maximale

Connexion Metabase → PostgreSQL
Lors de la configuration dans Metabase, utiliser les paramètres suivants :
ParamètreValeurTypePostgreSQLNom d'affichageMeteoDBHôtepostgresPort5432Nom de la basemeteo_dbUtilisateurmeteo_userMot de passemeteo_password

⚠️ Important : à l'intérieur de Metabase, l'hôte est postgres et non localhost.


Notes sur les fichiers de données
Le fichier CSV brut de Météo-France n'est pas versionné sur GitHub car il dépasse la limite de 100 Mo.
Les dossiers de données sont exclus via .gitignore :
data/raw/
data/clean/

Workflow Git
Le projet utilise une branche dédiée pour les travaux de data engineering :
bashgit checkout yasmine-setup
Commandes pour pousser les modifications :
bashgit add scripts/
git add README.md
git add docker-compose.yml
git add notebooks/
git commit -m "Finalize data engineering pipeline"
git push

Rôle : Data Engineer
Ce rôle couvre les responsabilités suivantes :

mise en place du dépôt GitHub et de la structure du projet
configuration de Docker et de PostgreSQL
connexion de Metabase à PostgreSQL
nettoyage du dataset Météo-France
création de la table PostgreSQL meteo_daily
développement des scripts ETL réutilisables
documentation technique complète


Prochaines étapes
L'équipe dashboard peut désormais utiliser Metabase pour :

créer des visualisations (températures, précipitations, vent)
construire des dashboards interactifs avec filtres
importer les cartes GeoJSON pour les visualisations géographiques
préparer la démonstration finale du projet