from medpredictor import Config
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTENC

path_models = './src/models'
path_cod_data = './src/data_codified/enc_data.csv'
Config().create_dir(dir_path=path_models)

df_enc = pd.read_csv(path_cod_data)

# Set up the targets
X_h1 = df_enc.drop(columns=['MentHlth', 'PhysHlth', 'Stroke_enc', 'HeartDiseaseorAttack_enc',
                            'Diabetes_012_enc', 'CholCheck_enc',
                            'AnyHealthcare_enc', 'NoDocbcCost_enc',
                            'Education_enc', 'Income_enc' 
                            ])
y_h1 = df_enc['Diabetes_012_enc']

X_h2 = df_enc.drop(columns=['MentHlth', 'PhysHlth', 'Diabetes_012_enc', 'HeartDiseaseorAttack_enc',
                            'Stroke_enc', 'AnyHealthcare_enc',
                            'NoDocbcCost_enc', 'Education_enc',
                            'Income_enc'])
y_h2 = df_enc['Stroke_enc']

X_h3 = df_enc.drop(columns=['MentHlth', 'PhysHlth',
                            'HeartDiseaseorAttack_enc','AnyHealthcare_enc',
                            'NoDocbcCost_enc', 'Education_enc',
                            'Income_enc'])
y_h3 = df_enc['HeartDiseaseorAttack_enc']

# Model for hypothesis 1
X_train, X_test, y_train, y_test = train_test_split(X_h1, y_h1, test_size=0.3, random_state=42)

sm = SMOTENC(categorical_features=list(range(len(X_h1.columns)-1)))
X_train_resampled, y_train_resampled = sm.fit_resample(X_train, y_train)

# KNN
knn_h1 = KNeighborsClassifier(n_neighbors=3)
knn_h1.fit(X_train_resampled, y_train_resampled)

with open(path_models + '/knn_h1_model.pkl', "wb") as model_h1_file:
    pickle.dump(knn_h1, model_h1_file)

# Model for hypothesis 2
X_train, X_test, y_train, y_test = train_test_split(X_h2, y_h2, test_size=0.3, random_state=42)

sm = SMOTENC(categorical_features=list(range(len(X_h2.columns)-1)))
X_train_resampled, y_train_resampled = sm.fit_resample(X_train, y_train)

# Random forest
rf_h2 = RandomForestClassifier(n_estimators=28,
                            max_depth=18)
rf_h2.fit(X_train_resampled, y_train_resampled)

with open(path_models + '/rf_h2_model.pkl', "wb") as model_h2_file:
    pickle.dump(rf_h2, model_h2_file)

# Model for hypothesis 3
X_train, X_test, y_train, y_test = train_test_split(X_h3, y_h3, test_size=0.3, random_state=42)

sm = SMOTENC(categorical_features=list(range(len(X_h3.columns)-1)))
X_train_resampled, y_train_resampled = sm.fit_resample(X_train, y_train)

# Random forest
rf_h3 = RandomForestClassifier(n_estimators=22,
                            max_depth=17)
rf_h3.fit(X_train_resampled, y_train_resampled)

with open(path_models + '/rf_h3_model.pkl', "wb") as model_h3_file:
    pickle.dump(rf_h3, model_h3_file)