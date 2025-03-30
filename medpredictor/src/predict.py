import pickle
import pandas as pd


def make_h1_prediction():
    path_survey_answers = './src/answers/answers_codified.csv'
    path_h1_model = './src/models/knn_h1_model.pkl'
    
    with open(path_h1_model, "rb") as model_h1_file:
        model_h1 = pickle.load(model_h1_file)
    
    y = pd.read_csv(path_survey_answers)
    diabetes = model_h1.predict(y)
    return int(diabetes[0])

def make_h2_prediction():
    path_survey_answers = './src/answers/answers_codified.csv'
    path_h2_model = './src/models/rf_h2_model.pkl'

    with open(path_h2_model, "rb") as model_h2_file:
        model_h2 = pickle.load(model_h2_file)

    y = pd.read_csv(path_survey_answers)
    stroke = model_h2.predict(y)
    return int(stroke[0])

def make_h3_prediction():
    path_survey_answers = './src/answers/answers_codified.csv'
    path_h3_model = './src/models/rf_h3_model.pkl'

    with open(path_h3_model, "rb") as model_h3_file:
        model_h3 = pickle.load(model_h3_file)
    
    y = pd.read_csv(path_survey_answers)
    heart_attack = model_h3.predict(y)
    return int(heart_attack[0])