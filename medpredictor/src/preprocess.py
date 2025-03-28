from medpredictor import Config, Utils, Encoder
import pandas as pd

data_codified_path = './src/data_codified'
Config().create_dir(dir_path=data_codified_path)

df_enc_dict = {}

df_dec_dict = {}

orders = {}

enc = Encoder()

num_columns = ['BMI', 'MentHlth', 'PhysHlth']

orders = {'Age': Utils.values_age_order,
          'GenHlth': Utils.values_status_order,
          'Income': Utils.values_income_order,
          'Education': Utils.values_education_order,
          'Diabetes_012': Utils.values_diabetes_order}

# Set up the data frame
df = pd.read_csv(Config.data_cleaned_path)

df_copy = df.drop(columns=num_columns)

# Feature codification
for column in df_copy.columns:
    order = orders.get(column, None)
    if order is not None:
        enc_, dec_ = enc.ordinal_encoder_method(df=df_copy, 
                                          column_name=column, 
                                          order=order)
        df_enc_dict[column] = pd.DataFrame({column + '_enc': enc_})
        df_dec_dict[column] = pd.DataFrame({column + '_dec': dec_})
        continue
    enc_, dec_ = enc.label_encoder_method(df=df_copy,
                                    column_name=column)
    df_enc_dict[column] = pd.DataFrame({column + '_enc': enc_})
    df_dec_dict[column] = pd.DataFrame({column + '_dec': dec_})

df_numerics = enc.robust_scaler_method(df=df, columns_name=num_columns)

df_enc_dict.update({'numerics':df_numerics})

df_enc = pd.concat(list(df_enc_dict.values()), axis=1)
df_dec = pd.concat(list(df_dec_dict.values()), axis=1)

df_enc.to_csv(data_codified_path + '/enc_data.csv', index=False)
df_dec.to_csv(data_codified_path + '/dec_data.csv', index=False)