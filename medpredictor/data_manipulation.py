import pandas as pd

class DataFrameOperations:
    def __init__(self, df):
        self.df = df
        pass

    def create_combined_column(self, new_column_name, column_1, column_2,criterion):
        self.df[new_column_name] = [criterion(value_1, value_2) for value_1, value_2 in zip(self.df[column_1], self.df[column_2])]
        return
    

    

