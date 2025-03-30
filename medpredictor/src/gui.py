from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QProgressBar
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, Signal, QThread
import time
import os
import preprocess
import train

class ProcessingDataThread(QThread):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        not_created = True
        for i in range(101):
            self.progress.emit(i)
            self.msleep(50)
            if not_created:
                start_time = time.time()
                preprocess.preprocess_data()
                end_time = time.time()
                not_created = False
        print(f"Time for data processing: {round(end_time - start_time, 2)} secs")
        self.finished.emit()

class ProcessingDataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Processing data")
        self.setGeometry(150, 150, 400, 200)
        self.setWindowIcon(QIcon("./src/static/medpredictor_icon.png"))

        layout = QVBoxLayout()

        if not os.path.exists('./src/data_codified'): 
            self.title_label = QLabel("Processing data...")
            self.title_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.title_label)

            self.progress_bar = QProgressBar()
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(0)
            layout.addWidget(self.progress_bar)
    

            self.processing_data_thread = ProcessingDataThread()
            self.processing_data_thread.progress.connect(self.update_progress)
            self.processing_data_thread.finished.connect(lambda: self.update_title("Data processed!"))
            self.processing_data_thread.finished.connect(self.close)
            self.processing_data_thread.start()
        else:
            self.title_label = QLabel("Data already processed!")
            self.title_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.title_label)
            
            self.progress_bar = QProgressBar()
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(100)
            layout.addWidget(self.progress_bar)

            self.train_models_button = QPushButton("Train models!")
            layout.addWidget(self.train_models_button)

        self.setLayout(layout)
        
    def update_progress(self, value):
        self.progress_bar.setValue(value)
    
    def update_title(self, title):
        self.title_label.setText(title)
        self.setWindowTitle(title)

class TrainingModelThread(QThread):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        total_models = 3
        start_time = time.time()
        self.progress.emit(0)
        train.train_model_h1()
        self.progress.emit(int((1 / total_models) * 100))
        
        train.train_model_h2()
        self.progress.emit(int((2 / total_models) * 100))

        train.train_model_h3()
        self.progress.emit(100)
        end_time = time.time()
        print(f"Time for training models: {round(end_time - start_time, 2)} secs")
        self.finished.emit()

class TrainingModelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training Model")
        self.setGeometry(150, 150, 400, 200)
        self.setWindowIcon(QIcon("./src/static/medpredictor_icon.png"))

        layout = QVBoxLayout()
        
        if not os.path.exists('./src/models'):
            self.title_label = QLabel("Training models...")
            self.title_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.title_label)

            self.progress_bar = QProgressBar()
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(0)
            layout.addWidget(self.progress_bar)

            self.training_model_thread = TrainingModelThread()
            self.training_model_thread.progress.connect(self.update_progress)
            self.training_model_thread.finished.connect(lambda: self.update_title("Training completed!"))
            self.training_model_thread.finished.connect(self.close)
            self.training_model_thread.start()
        else:
            self.title_label = QLabel("Training already done!")
            self.title_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.title_label)
            
            self.progress_bar = QProgressBar()
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(100)
            layout.addWidget(self.progress_bar)
            

        self.setLayout(layout)
        
    def update_progress(self, value):
        self.progress_bar.setValue(value)
    
    def update_title(self, title):
        self.title_label.setText(title)
        self.setWindowTitle(title)

class SurveyWindow(QWidget):
    answers_submitted = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MedPredictor Survey")
        self.setGeometry(100, 100, 400, 500)
        self.setWindowIcon(QIcon("./src/static/medpredictor_icon.png"))

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Age"))
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter your age")
        self.age_input.textChanged.connect(self.validate_age)
        layout.addWidget(self.age_input)

        layout.addWidget(QLabel("Sex"))
        self.sex_input = QComboBox()
        self.sex_input.addItems(["Male", "Female"])
        layout.addWidget(self.sex_input)

        layout.addWidget(QLabel("Body Mass Index (BMI)"))
        self.bmi_input = QLineEdit()
        self.bmi_input.setPlaceholderText("Enter your BMI")
        self.bmi_input.textChanged.connect(self.validate_bmi)
        layout.addWidget(self.bmi_input)

        layout.addWidget(QLabel("Do you consume vegetables one or more times per day?"))
        self.veggie_input = QComboBox()
        self.veggie_input.addItems(["Yes", "No"])
        layout.addWidget(self.veggie_input)

        layout.addWidget(QLabel("Do you consume fruits one or more times per day?"))
        self.fruits_input = QComboBox()
        self.fruits_input.addItems(["Yes", "No"])
        layout.addWidget(self.fruits_input)

        layout.addWidget(QLabel("Have you ever smoked at least 100 cigarettes in your entire life?"))
        self.smoker_input = QComboBox()
        self.smoker_input.addItems(["Yes", "No"])
        layout.addWidget(self.smoker_input)

        layout.addWidget(QLabel("Do you consume X drinks per week? (For adult men: X>=14. For adult women: X>=7)"))
        self.alcohol_input = QComboBox()
        self.alcohol_input.addItems(["Yes", "No"])
        layout.addWidget(self.alcohol_input)

        layout.addWidget(QLabel("Do you have high blood pressure?"))
        self.highbp_input = QComboBox()
        self.highbp_input.addItems(["Yes", "No"])
        layout.addWidget(self.highbp_input)

        layout.addWidget(QLabel("Do you have high cholesterol?"))
        self.highchol_input = QComboBox()
        self.highchol_input.addItems(["Yes", "No"])
        layout.addWidget(self.highchol_input)

        layout.addWidget(QLabel("Do you have serious difficulty walking?"))
        self.diffwalk_input = QComboBox()
        self.diffwalk_input.addItems(["Yes", "No"])
        layout.addWidget(self.diffwalk_input)

        layout.addWidget(QLabel("Have you been physically active in the last 30 days?"))
        self.physact_input = QComboBox()
        self.physact_input.addItems(["Yes", "No"])
        layout.addWidget(self.physact_input)
        
        layout.addWidget(QLabel("Would you say that in general your health is..."))
        self.health_input = QComboBox()
        self.health_input.addItems(["Excellent", "Very good", "Good", "Fair", "Poor"])
        layout.addWidget(self.health_input)

        self.submit_button = QPushButton("Submit answers")
        self.submit_button.clicked.connect(self.collect_data)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def validate_age(self):
        text = self.age_input.text()
        if not text.isdigit():
            self.age_input.setText("" if text else text)
    
    def validate_bmi(self):
        text = self.bmi_input.text()
        try:
            if text and float(text) < 0:
                self.bmi_input.setText("")
        except ValueError:
            self.bmi_input.setText("")
    
    def collect_data(self):
        answers = {
            "Age": int(self.age_input.text() if self.age_input.text().isdigit() else None),
            "Sex": self.sex_input.currentText(),
            "BMI": float(self.bmi_input.text()) if self.bmi_input.text() else None,
            "Veggie": self.veggie_input.currentText(),
            "Fruits": self.fruits_input.currentText(),
            "Smoker": self.smoker_input.currentText(),
            "HvyAlcoholConsump": self.alcohol_input.currentText(),
            "HighBP": self.highbp_input.currentText(),
            "HighChol": self.highchol_input.currentText(),
            "DiffWalk": self.diffwalk_input.currentText(),
            "PhysActivity": self.physact_input.currentText(),
            "GenHlth": self.health_input.currentText()
            }
        self.answers_submitted.emit(answers)
        self.close()
        
class MedPredictorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medpredictor App")
        self.setGeometry(100, 100, 500, 400)
        self.setWindowIcon(QIcon("./src/static/medpredictor_icon.png"))

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Welcome to Medpredictor App!")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        description = QLabel("""This app implements machine learning models to predict the likelihood of having diabetes,  
            as well as stroke and heart attack, based on your demographics, habits, and physical conditions.""")
        description.setFont(QFont("Arial", 12))
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)

        warning_box = QLabel("Warning")
        warning_box.setFont(QFont("Arial", 12, QFont.Bold))
        warning_box.setStyleSheet("background-color: yellow; color: black; padding: 8px; border: 2px solid black; border-radius: 5px;")
        warning_box.setAlignment(Qt.AlignCenter)
        layout.addWidget(warning_box)

        disclaimer = QLabel("This project is purely practical and should not be taken as a real diagnosis.")
        disclaimer.setFont(QFont("Arial", 12))
        disclaimer.setAlignment(Qt.AlignCenter)
        layout.addWidget(disclaimer)

        self.start_button = QPushButton("Begin")
        self.start_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.start_button.setStyleSheet("background-color: green; color: white; padding: 8px; border: 2px solid white; border-radius: 5px;")
        self.start_button.clicked.connect(self.start_survey)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
    
    def train_model(self):
        if not hasattr(self, "training_model"):  
            self.training_model = TrainingModelWindow()
            self.training_model.show()

    def start_training_model(self):
        if not hasattr(self, "processing_data"):
            self.processing_data = ProcessingDataWindow()
            self.processing_data.show()
            if hasattr(self.processing_data, "processing_data_thread"):
                self.processing_data.processing_data_thread.finished.connect(self.train_model)
            else:
                self.processing_data.train_models_button.clicked.connect(self.train_model)
                self.processing_data.train_models_button.clicked.connect(self.processing_data.close)
                

    def start_survey(self):
        self.survey_window = SurveyWindow()
        self.survey_window.answers_submitted.connect(preprocess.preprocess_answers)
        self.survey_window.answers_submitted.connect(self.start_training_model)
        self.survey_window.show()
        self.close()
    
   
        
   


