from medpredictor import Config, Utils, Encoder
import pandas as pd


def answers_encoder(df):
    df_enc_dict = {}

    df_dec_dict = {}

    enc = Encoder()

    orders = {'Age': Utils.values_age_order,
              'Sex': Utils.values_sex_order,
              'Veggies': ["No", "Yes"],
              'Fruits': ["No", "Yes"],
              'Smoker': ["No", "Yes"],
              'HvyAlcoholConsump': ["No", "Yes"],
              'HighBP': ["No", "Yes"],
              'HighChol': ["No", "Yes"],
              'DiffWalk': ["No", "Yes"],
              'PhysActivity': ["No", "Yes"],
              'GenHlth': Utils.values_status_order
              }

    for column in df.columns:
        order = orders.get(column, None)
        if order is not None:
            enc_, dec_ = enc.ordinal_encoder_method(df=df, 
                                            column_name=column, 
                                            order=order)
            df_enc_dict[column] = pd.DataFrame({column + '_enc': enc_})
            df_dec_dict[column] = pd.DataFrame({column + '_dec': dec_})
            continue
    df_enc_dict.update({"BMI": df["BMI"]})
    df_dec_dict.update({"BMI": df["BMI"]})

    df_enc = pd.concat(list(df_enc_dict.values()), axis=1)
    df_dec = pd.concat(list(df_dec_dict.values()), axis=1)
    return df_enc, df_dec

def data_encoder(df):
    df_enc_dict = {}

    df_dec_dict = {}

    enc = Encoder()

    orders = {'Age': Utils.values_age_order,
            'Sex': Utils.values_sex_order,
            'GenHlth': Utils.values_status_order,
            'Income': Utils.values_income_order,
            'Education': Utils.values_education_order,
            'Diabetes_012': Utils.values_diabetes_order
            }
    
    num_columns = ['BMI', 'MentHlth', 'PhysHlth']

    df_copy = df.copy().drop(columns=num_columns)

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
    return df_enc, df_dec

def preprocess_answers(answers):
    answers_path = './src/answers'
    Config().create_dir(dir_path=answers_path)
    answers.update({"Age": Utils().transform_age(answers["Age"])})
    df = pd.DataFrame({"HighBP": [answers["HighBP"]],
                       "HighChol": [answers["HighChol"]],
                       "Smoker": [answers["Smoker"]],
                       "PhysActivity": [answers["PhysActivity"]],
                       "Fruits": [answers["Fruits"]],
                       "Veggies": [answers["Veggies"]],
                       "HvyAlcoholConsump": [answers["HvyAlcoholConsump"]],
                       "GenHlth": [answers["GenHlth"]],
                       "DiffWalk": [answers["DiffWalk"]],
                       "Sex": [answers["Sex"]],
                       "Age": [answers["Age"]],
                       "BMI": [answers["BMI"]]                    
            })
    df_enc, df_dec = answers_encoder(df)

    df_enc.to_csv(answers_path + '/answers_codified.csv', index=False)
    df_dec.to_csv(answers_path + '/answers.csv', index=False)
    return

def preprocess_data():
    data_codified_path = './src/data_codified'
    Config().create_dir(dir_path=data_codified_path)

    df = pd.read_csv(Config.data_cleaned_path)
    
    df_enc, df_dec = data_encoder(df)

    df_enc.to_csv(data_codified_path + '/enc_data.csv', index=False)
    df_dec.to_csv(data_codified_path + '/dec_data.csv', index=False)
    return