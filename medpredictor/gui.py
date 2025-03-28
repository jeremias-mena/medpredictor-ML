from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
import sys

class MedPredictorSurveyApp(QWidget):
    def __init__(self):
        super().__init__
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
        