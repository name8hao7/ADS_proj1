from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
TLC_DATA_DIR = RAW_DATA_DIR / "tlc"
EXTERNAL_DATA_DIR = RAW_DATA_DIR / "external"
ZONES_DATA_DIR = RAW_DATA_DIR / "zones"

INTERIM_DATA_DIR = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
PLOTS_DIR = PROJECT_ROOT / "plots"

YEAR = 2024
MONTHS = list(range(1, 7))
SERVICE_TYPES = ["yellow", "green", "hvfhv"]
