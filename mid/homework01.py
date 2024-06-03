import os
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QVBoxLayout, QLabel)
from PySide6.QtCore import Qt

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello World!')
        self.setGeometry(100, 300, 200, 100)
        self.layout = QVBoxLayout()
        self.label_01 = QLabel('Hello World!')
        self.label_01.setAlignment(Qt.AlignCenter)
        
        directory_path = os.path.dirname(os.path.realpath(__file__))
        self.label_02 = QLabel('Main script 경로:' + directory_path)
        self.label_02.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(self.label_01)
        self.layout.addWidget(self.label_02)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec_())