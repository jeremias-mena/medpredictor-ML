from medpredictor import Graph, Encoder, Config, Utils
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from imblearn.over_sampling import SMOTENC

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

def model_metrics(y_test, y_pred, average):
    met = {'Accuracy':round((metrics.accuracy_score(y_test, y_pred) * 100), 2),
              'Recall': round((metrics.recall_score(y_test, y_pred, average=average) * 100), 2),
              'Precision': round((metrics.precision_score(y_test, y_pred, average=average) * 100), 2),
              'F1-score': round((metrics.f1_score(y_test, y_pred, average=average) * 100), 2)
              }
    return met

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

# Set up the targets
X_h1 = df_enc.drop(columns=['MentHlth', 'PhysHlth',
                            'Diabetes_012_enc', 'CholCheck_enc',
                            'AnyHealthcare_enc', 'NoDocbcCost_enc',
                            'Education_enc', 'Income_enc' 
                            ])
y_h1 = df_enc['Diabetes_012_enc']

X_h2 = df_enc.drop(columns=['MentHlth', 'PhysHlth',
                            'Stroke_enc', 'AnyHealthcare_enc',
                            'NoDocbcCost_enc', 'Education_enc',
                            'Income_enc'])
y_h2 = df_enc['Stroke_enc']

X_h3 = df_enc.drop(columns=['MentHlth', 'PhysHlth',
                            'HeartDiseaseorAttack_enc','AnyHealthcare_enc',
                            'NoDocbcCost_enc', 'Education_enc',
                            'Income_enc'])
y_h3 = df_enc['HeartDiseaseorAttack_enc']

