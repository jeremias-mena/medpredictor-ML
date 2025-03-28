from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

class ResultsWindow(QWidget):
     def __init__(self, results):
        super().__init__()
        self.setWindowTitle("Your Results")
        self.setGeometry(150, 150, 400, 300)

        layout = QVBoxLayout()

        title = QLabel("Your Results")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        for result in results:
            label = QLabel(result)
            label.setFont(QFont("Arial", 12))
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        self.setLayout(layout)

class SurveyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MedPredictor Survey")
        self.setGeometry(100, 100, 400, 500)

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

        self.yn_inputs = {}
        questions = {
            "Veggie": "Do you consume vegetables one or more times per day?",
            "Fruits": "Do you consume fruits one or more times per day?",
            "Smoker": "Have you ever smoked at least 100 cigarettes in your entire life?",
            "HvyAlcoholConsump": "Do you consume X drinks per week?",
            "HighBP": "Do you have high blood pressure?",
            "HighChol": "Do you have high cholesterol?",
            "DiffWalk": "Do you have serious difficulty walking?",
            "PhysActivity": "Have you been physically active in the last 30 days?"
        }

        for key, question in questions.items():
            layout.addWidget(QLabel(question))
            combo = QComboBox()
            combo.addItems(["Yes", "No"])
            layout.addWidget(combo)
            self.yn_inputs[key] = combo
        
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
        self.age = int(self.age_input.text() if self.age_input.text().isdigit() else None)
        self.sex = self.sex_input.currentText()
        self.bmi = float(self.bmi_input.text()) if self.bmi_input.text() else None
        self.answers = {key: combo.currentText() for key, combo in self.yn_inputs.items()}
        self.general_health = self.health_input.currentText()

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medpredictor App")
        self.setGeometry(100, 100, 500, 400)
        self.setWindowIcon(QIcon("icon.png"))

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
    
    def start_survey(self):
        self.survey_window = SurveyWindow()
        self.survey_window.show()
        self.close()
   


