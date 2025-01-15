from pathlib import Path 

class Config:
    data_dir_raw = Path(__file__).resolve().parent / 'data/raw'
    data_dir_processed = Path(__file__).resolve().parent / 'data/processed'
    data_dir_cleaned = Path(__file__).resolve().parent / 'data/cleaned'

    data_raw_path = data_dir_raw/'diabetes_012_health_indicators_BRFSS2015.csv'
    data_export_processed = data_dir_processed/'diabetes_processed.csv'
    data_export_cleaned = data_dir_cleaned/'diabetes_cleaned.csv'
