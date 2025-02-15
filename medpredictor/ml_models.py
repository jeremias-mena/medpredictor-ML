from medpredictor import Graph, Encoder, Config, Utils
import pandas as pd
from time import perf_counter
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
              'F1-Score': round((metrics.f1_score(y_test, y_pred, average=average) * 100), 2)
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

# Models for hypothesis 1
X_train, X_test, y_train, y_test = train_test_split(X_h1, y_h1, test_size=0.3, random_state=42)

sm = SMOTENC(categorical_features=list(range(len(X_h1.columns)-1)))
X_train_resampled, y_train_resampled = sm.fit_resample(X_train, y_train)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)

start_f_h1_knn = perf_counter()
knn.fit(X_train_resampled, y_train_resampled)
end_f_h1_knn = perf_counter()

start_pred_h1_knn = perf_counter()
y_pred_h1_knn = knn.predict(X_test)
end_pred_h1_knn = perf_counter()

met_h1_knn = model_metrics(y_test, y_pred_h1_knn, 'weighted')

met_row_h1_knn = pd.DataFrame({'Hypotesis': ["How do a person's demographic characteristics, habits and physical conditions influence the likelihood of developing diabetes, according to the indicator recorded?"],
              'Model': ['K-Nearest Neighbors'],
              'Train time': [end_f_h1_knn - start_f_h1_knn],
              'Predict time': [end_pred_h1_knn - start_pred_h1_knn],
              'Accuracy': met_h1_knn['Accuracy'],
              'Recall': met_h1_knn['Recall'],
              'Precision': met_h1_knn['Precision'],
              'F1-Score': met_h1_knn['F1-Score']})

# Random forest
rf = RandomForestClassifier(n_estimators=22,
                            max_depth=17)
start_f_h1_rf = perf_counter()
rf.fit(X_train_resampled, y_train_resampled)
end_f_h1_rf = perf_counter()

start_pred_h1_rf = perf_counter()
y_pred_h1_rf = rf.predict(X_test)
end_pred_h1_rf = perf_counter()

met_h1_rf = model_metrics(y_test, y_pred_h1_rf, 'weighted')

met_row_h1_rf = pd.DataFrame({'Hypotesis': ["How do a person's demographic characteristics, habits and physical conditions influence the likelihood of developing diabetes, according to the indicator recorded?"],
              'Model': ['Random Forest'],
              'Train time': [end_f_h1_rf - start_f_h1_rf],
              'Predict time': [end_pred_h1_rf - start_pred_h1_rf],
              'Accuracy': met_h1_rf['Accuracy'],
              'Recall': met_h1_rf['Recall'],
              'Precision': met_h1_rf['Precision'],
              'F1-Score': met_h1_rf['F1-Score']})


# Models for hypothesis 2
X_train, X_test, y_train, y_test = train_test_split(X_h2, y_h2, test_size=0.3, random_state=42)

sm = SMOTENC(categorical_features=list(range(len(X_h2.columns)-1)))
X_train_resampled, y_train_resampled = sm.fit_resample(X_train, y_train)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)

start_f_h2_knn = perf_counter()
knn.fit(X_train_resampled, y_train_resampled)
end_f_h2_knn = perf_counter()

start_pred_h2_knn = perf_counter()
y_pred_h2_knn = knn.predict(X_test)
end_pred_h2_knn = perf_counter()

met_h2_knn = model_metrics(y_test, y_pred_h2_knn, 'binary')

met_row_h2_knn = pd.DataFrame({'Hypotesis': ["How do a person's demographics, habits and physical conditions influence the likelihood of having a stroke?"],
              'Model': ['K-Nearest Neighbors'],
              'Train time': [end_f_h2_knn - start_f_h2_knn],
              'Predict time': [end_pred_h2_knn - start_pred_h2_knn],
              'Accuracy': met_h2_knn['Accuracy'],
              'Recall': met_h2_knn['Recall'],
              'Precision': met_h2_knn['Precision'],
              'F1-Score': met_h2_knn['F1-Score']})

# Random forest
rf = RandomForestClassifier(n_estimators=28,
                            max_depth=18)
start_f_h2_rf = perf_counter()
rf.fit(X_train_resampled, y_train_resampled)
end_f_h2_rf = perf_counter()

start_pred_h2_rf = perf_counter()
y_pred_h2_rf = rf.predict(X_test)
end_pred_h2_rf = perf_counter()

met_h2_rf = model_metrics(y_test, y_pred_h2_rf, 'binary')

met_row_h2_rf = pd.DataFrame({'Hypotesis': ["How do a person's demographics, habits and physical conditions influence the likelihood of having a stroke?"],
              'Model': ['Random Forest'],
              'Train time': [end_f_h2_rf - start_f_h2_rf],
              'Predict time': [end_pred_h2_rf - start_pred_h2_rf],
              'Accuracy': met_h2_rf['Accuracy'],
              'Recall': met_h2_rf['Recall'],
              'Precision': met_h2_rf['Precision'],
              'F1-Score': met_h2_rf['F1-Score']})

# Models for hypothesis 3
X_train, X_test, y_train, y_test = train_test_split(X_h3, y_h3, test_size=0.3, random_state=42)

sm = SMOTENC(categorical_features=list(range(len(X_h3.columns)-1)))
X_train_resampled, y_train_resampled = sm.fit_resample(X_train, y_train)

# KNN
knn = KNeighborsClassifier(n_neighbors=3)

start_f_h3_knn = perf_counter()
knn.fit(X_train_resampled, y_train_resampled)
end_f_h3_knn = perf_counter()

start_pred_h3_knn = perf_counter()
y_pred_h3_knn = knn.predict(X_test)
end_pred_h3_knn = perf_counter()

met_h3_knn = model_metrics(y_test, y_pred_h3_knn, 'binary')

met_row_h3_knn = pd.DataFrame({'Hypotesis': ["How do a person's demographics, habits and physical conditions influence the likelihood of having a heart attack?"],
              'Model': ['K-Nearest Neighbors'],
              'Train time': [end_f_h3_knn - start_f_h3_knn],
              'Predict time': [end_pred_h3_knn - start_pred_h3_knn],
              'Accuracy': met_h3_knn['Accuracy'],
              'Recall': met_h3_knn['Recall'],
              'Precision': met_h3_knn['Precision'],
              'F1-Score': met_h3_knn['F1-Score']})

# Random forest
rf = RandomForestClassifier(n_estimators=22,
                            max_depth=17)
start_f_h3_rf = perf_counter()
rf.fit(X_train_resampled, y_train_resampled)
end_f_h3_rf = perf_counter()

start_pred_h3_rf = perf_counter()
y_pred_h3_rf = rf.predict(X_test)
end_pred_h3_rf = perf_counter()

met_h3_rf = model_metrics(y_test, y_pred_h3_rf, 'binary')

met_row_h3_rf = pd.DataFrame({'Hypotesis': ["How do a person's demographics, habits and physical conditions influence the likelihood of having a heart attack?"],
              'Model': ['Random Forest'],
              'Train time': [end_f_h3_rf - start_f_h3_rf],
              'Predict time': [end_pred_h3_rf - start_pred_h3_rf],
              'Accuracy': met_h3_rf['Accuracy'],
              'Recall': met_h3_rf['Recall'],
              'Precision': met_h3_rf['Precision'],
              'F1-Score': met_h3_rf['F1-Score']})

df_metrics = pd.concat([met_row_h1_knn, met_row_h1_rf,
                        met_row_h2_knn, met_row_h2_rf,
                        met_row_h3_knn, met_row_h3_rf], ignore_index=True)

df_metrics.to_csv(Config.model_metrics, index=False)