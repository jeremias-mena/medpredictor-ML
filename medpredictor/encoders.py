from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, RobustScaler
import pandas as pd

class Encoder():
    def __init__(self):
        pass

    def robust_scaler_method(self, df, columns_name):
        scaler = RobustScaler()
        df_num = pd.DataFrame(columns=columns_name)
        for column in columns_name:
            df_num[column] = scaler.fit_transform(df[[column]])
        return df_num 
    
    def label_encoder_method(self, df, column_name):
        enc = LabelEncoder()
        enc_data = enc.fit_transform(df[column_name])
        dec_data = enc.inverse_transform(enc_data)
        return enc_data, dec_data
    
    def ordinal_encoder_method(self, df, column_name, order):
        enc = OrdinalEncoder(categories=[order])
        enc_data = enc.fit_transform(df[[column_name]])
        dec_data = enc.inverse_transform(enc_data)
        return enc_data, dec_data
    
    
    
