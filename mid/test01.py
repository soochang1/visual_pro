import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QRadioButton, QVBoxLayout, QCheckBox)

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initial_ui()
        
    def initial_ui(self):
        self.setGeometry(200,100,400,200)
        self.setWindowTitle('die')
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        
        self.central_widget = QWidget()  
        self.setCentralWidget(self.central_widget) 
        
        self.label01 = QCheckBox('1. faith')
        self.label02 = QCheckBox('2. hope')
        self.label03 = QCheckBox('3. love')
        self.label04 = QLabel('')
        
        lm = QVBoxLayout()
        lm.addWidget(QLabel('What is most important?'))
        lm.addWidget(self.label01)
        lm.addWidget(self.label02)
        lm.addWidget(self.label03) 
        lm.addWidget(self.label04)
        
        self.central_widget.setLayout(lm)
    
        
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())
    

