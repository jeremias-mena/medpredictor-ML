import pandas as pd

class DataFrameOperations:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"Attibute {self.df} must be pandas.core.frame.DataFrame.")
        self.df = df
        pass

    def create_combined_column(self, new_column_name, column_1, column_2, criterion):
        self.df[new_column_name] = [criterion(value_1, value_2) for value_1, value_2 in zip(self.df[column_1], self.df[column_2])]
        return self.df
    
    def column_identifier(self, column_1, column_2, values_subset):
        column_1_values = self.df[column_1].unique()
        column_2_values = self.df[column_2].unique()
        
        if values_subset.issubset(column_1_values):
            variable_column, filter_column = column_1, column_2
        elif values_subset.issubset(column_2_values):
            variable_column, filter_column = column_2, column_1
        else:
            raise ValueError("Cannot identify columns properly.")
        return variable_column, filter_column
    
    def create_column_from_function(self, new_column_name, column_apply_function, function):
        self.df[new_column_name] = self.df[column_apply_function].apply(function)
        return self.df
    
    def filter_group_registers(self, column_1, column_2, condition):
        group = self.df.groupby([column_1, column_2]).size().reset_index(name='count')
        total_registers = group['count'].sum()

        results = {'result':group.loc[condition, 'count'].sum(), 'total_registers':total_registers} 
        
        return results
    

