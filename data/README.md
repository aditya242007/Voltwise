# Data

Place original datasets in `raw/`, derived intermediate data in `interim/`,
and model-ready data in `processed/`. No dataset is bundled. Record each
source, license, download date, timezone, units, and transformations. Do not
commit private or restricted data; these folders are ignored by Git.

The default configuration expects `data/processed/demand.csv` with `timestamp`
and numeric `demand` columns. Update `configs/config.yaml` as needed.