# MAST30034 Project 1: Subway Accessibility and Ride Demand in NYC

## Project Overview

This project investigates how subway accessibility is associated with taxi and ride-hailing demand across New York City. The analysis combines NYC TLC trip records with an external MTA subway station dataset and taxi zone spatial data.

The main research question is:

> How is subway accessibility associated with taxi and ride-hailing demand intensity and driver earning efficiency across NYC taxi zones?

The project focuses on three TLC service types:

- Yellow taxi
- Green taxi
- High Volume For-Hire Vehicles (HVFHV)

The analysis period is January to June 2024.

## Key Idea

The project studies whether taxi zones with stronger subway access have different travel demand and earning patterns. Subway accessibility is measured using:

- Number of subway stations within each taxi zone
- Distance from each taxi zone centroid to the nearest subway station
- A derived subway access level: low, medium, or high

The main outcome used for demand analysis is trip count at service-zone-hour level. Driver earning efficiency is explored as a secondary outcome.

## Repository Structure

```text
ADS_proj1/
├── data/
│   ├── raw/                 # raw TLC, subway, and taxi zone files; not committed
│   ├── interim/             # monthly aggregated intermediate outputs; not committed
│   └── processed/           # final processed datasets; not committed
├── notebooks/
│   ├── preprocessing.ipynb  # data cleaning, aggregation, and spatial feature creation
│   ├── EDA.ipynb            # exploratory analysis and visualisations
│   └── Modelling.ipynb      # OLS and Random Forest modelling
├── plots/                   # generated plots; not committed at this stage
├── report/                  # final report files will be added later
├── scripts/
│   └── config.py            # shared project configuration
├── requirements.txt
├── .gitignore
└── README.md
```

## Data Sources

Raw data files are not included in the repository because the TLC trip records are large.

Expected local data layout:

```text
data/raw/
├── tlc/
│   ├── yellow/
│   │   ├── yellow_tripdata_2024-01.parquet
│   │   ├── ...
│   │   └── yellow_tripdata_2024-06.parquet
│   ├── green/
│   │   ├── green_tripdata_2024-01.parquet
│   │   ├── ...
│   │   └── green_tripdata_2024-06.parquet
│   └── hvfhv/
│       ├── fhvhv_tripdata_2024-01.parquet
│       ├── ...
│       └── fhvhv_tripdata_2024-06.parquet
├── external/
│   └── mta_subway_stations.csv
└── zones/
    ├── taxi_zone_lookup.csv
    └── taxi_zones/
        ├── taxi_zones.shp
        ├── taxi_zones.shx
        ├── taxi_zones.dbf
        ├── taxi_zones.prj
        └── taxi_zones.cpg
```

Main sources:

- NYC TLC Trip Record Data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- MTA Subway Stations dataset
- NYC TLC Taxi Zone lookup and taxi zone shapefile

## Environment Setup

The project is intended to be run in a Linux or WSL environment with PySpark.

Example setup:

```bash
python3 -m venv ~/.venvs/mast30034
source ~/.venvs/mast30034/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name mast30034 --display-name "mast30034"
```

Required Python packages are listed in `requirements.txt`.

## Running the Project

Run the notebooks in this order:

1. `notebooks/preprocessing.ipynb`
2. `notebooks/EDA.ipynb`
3. `notebooks/Modelling.ipynb`

The preprocessing notebook reads raw TLC and external data, cleans invalid trips, aggregates trips to service-zone-hour level, creates subway accessibility features, and saves processed outputs.

The EDA notebook examines:

- Service-level demand differences
- Subway accessibility and trip demand
- Borough-level patterns
- Hourly demand and earning patterns
- Trip distance and duration patterns
- Spatial demand hotspots
- Airport-zone sensitivity checks

The modelling notebook compares:

- OLS Linear Regression
- Random Forest Regressor

The modelling target is `log_trip_count`, based on service-zone-hour level demand.

## Current Findings

The current analysis suggests that subway accessibility is associated with stronger ride demand, especially for HVFHV. This pattern remains after excluding airport zones. However, higher subway accessibility does not consistently translate into higher driver earning efficiency. A plausible explanation is that high-access zones generate many shorter trips, while lower-access zones generate fewer but longer trips.

Airport zones and Manhattan activity centres are important location effects and are treated carefully in the exploratory analysis.

## Notes

- Raw and processed data are ignored by Git due to file size.
- Generated plots are currently treated as reproducible outputs and are not committed.
- The final report will be added under `report/`.
- Yellow and green taxi earning variables are based on `total_amount`, while HVFHV uses `driver_pay`; cross-service earning comparisons should therefore be interpreted carefully.
