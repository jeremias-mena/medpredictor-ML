import pickle
import pandas as pd

path_h1_model = './src/models/knn_h1_model.pkl'
path_h2_model = './src/models/rf_h2_model.pkl'
path_h3_model = './src/models/rf_h3_model.pkl'

path_survey_answers = './src/answers/answers_codified.csv'

with open(path_h1_model, "rb") as model_h1_file:
    model_h1 = pickle.load(model_h1_file)

with open(path_h2_model, "rb") as model_h2_file:
    model_h2 = pickle.load(model_h2_file)

with open(path_h3_model, "rb") as model_h3_file:
    model_h3 = pickle.load(model_h3_file)

y = pd.read_csv(path_survey_answers)

diabetes = model_h1.predict(y)
stroke = model_h2.predict(y)
heart_attack = model_h3.predict(y)




