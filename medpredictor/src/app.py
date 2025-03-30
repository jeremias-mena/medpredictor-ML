import sys
from PySide6.QtWidgets import QApplication
from gui import MedPredictorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    med_pred_app = MedPredictorApp()
    med_pred_app.show()
    sys.exit(app.exec())

    


