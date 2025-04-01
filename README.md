# 🩺 MedPredictor-ML

## 📌 Description
This project implements Machine Learning models to predict the likelihood of a person suffering from diabetes 🩸, stroke 🧠 or heart attack ❤️. To do this, two main algorithms are used:

* 🌳 Random Forests (Random Forest).
* 🔍 k-Nearest Neighbors (k-NN)

The model takes into account several variables related to demographic factors 👥, dietary habits 🥗 and negative habits 🚬🍺, with the aim of providing a predictive analytical tool for health.

## 📊 Dataset
The dataset used to carry out this project is available at [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv). 

## 📂 Project structure
```
📁 mdepredictor-ML
├── 📂 medpredictor 
    ├── 📂 data
        ├── 📂 cleaned
        ├── 📂 processed
        ├── 📂 raw
    ├── 📂 notebooks
        ├── 01-data-processed.ipynb
        ├── 02-data-cleaned.ipynb
        ├── 03-exploratory-data-analysis.ipynb
        ├── 04-ML-models.ipynb
    ├── 📂 src
        ├── 📂 static                       
        ├── app.py             
        ├── gui.py
        ├── predict.py
        ├── preprocess.py
        ├── train.py
    ├── __init__.py             
    ├── config.py
    ├── data_manipulation.py
    ├── encoders.py
    ├── graphs.py
    ├── ml_models.py
    ├── utils.py      
├── .gitignore       
├── README.md  
├── requirements.txt 
├── setup.py
```  

## 🏃 Use
To start the application, you must perform the following steps:
1) Change to the `src` directory.
```
cd medpredictor/src
```
2) Run the application with the following script
```
python app.py
```

## ⚙️ Installation and Requirements
1) Clone this repository:
```
git clone https://github.com/jeremias-mena/medpredictor-ML.git
cd medpredictor-ML
```
2) To run this project, you'll need to install the dependencies and have Python 3.12.3
```
pip install -r requirements.txt
```

## 📈 Model evaluation

Models are evaluated using:

* 📊 Confusion matrix.

* 🎯 Accuracy, Precision, Recall and F1-score.

## 🤝 Contributions

If you would like to contribute, please open an issue or make a pull request with implementation improvements or analysis results.

## 📩 Contact

For questions or suggestions, please contact menajeremias08@gmail.com.

