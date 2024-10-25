import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        uic.loadUi('D:/3SBME26/3-Third Year/1-First Term/1-DSP/Tasks/Task 2/DSP-2-Sampling-Theory-Studio-/mainApp.ui', self)  # Ensure the correct path to the .ui file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
