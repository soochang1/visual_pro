import sys
from PySide6.QtWidgets import (QWidget, QApplication, QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel)
from PySide6.QtCore import Signal, Qt

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ENTER')
        self.setGeometry(100, 300, 200, 100)
        
        self.layout = QVBoxLayout()
        self.enter_button = QPushButton("ENTER")
        self.layout.addWidget(self.enter_button)
        self.setLayout(self.layout)
        
        self.enter_button.clicked.connect(self.show_dialog)
    
    def show_dialog(self):
        dialog = My_Signal(self)
        dialog.exec_()

class My_Signal(QDialog):
    # 커스텀 시그널 정의
    result_signal = Signal(int)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("ENTER After")
        
        lm = QVBoxLayout()
        self.label = QLabel("Enter an integer:")
        self.input_line = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)
        
        lm.addWidget(self.label)
        lm.addWidget(self.input_line)
        lm.addWidget(self.ok_button)
        self.setLayout(lm)
        self.show()
                
    def ok_clicked(self):
        try:
            value = int(self.input_line.text())
            self.accept()
            # 입력된 값을 시그널로 emit
            self.result_signal.emit(value)
            print("입력된 값:", value)
        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec())