from pathlib import Path 
import os
import re

class Config:
    data_dir_raw = Path(__file__).resolve().parent / 'data/raw'
    data_dir_processed = Path(__file__).resolve().parent / 'data/processed'
    data_dir_cleaned = Path(__file__).resolve().parent / 'data/cleaned'
    model_dir_metrics = Path(__file__).resolve().parent / 'model-metrics'

    data_raw_path = data_dir_raw/'diabetes_012_health_indicators_BRFSS2015.csv'
    data_processed_path = data_dir_processed/'diabetes_processed.csv'
    data_cleaned_path = data_dir_cleaned/'diabetes_cleaned.csv'
    model_metrics = model_dir_metrics/'model_metrics.csv'

    def __init__(self):
        pass
    
    def create_dir(self, dir_path: str) -> None:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    def check_files(self, path):
        return any(re.search(r"\.pkl$", file) for file in os.listdir(path)) if os.path.exists(path) else False


