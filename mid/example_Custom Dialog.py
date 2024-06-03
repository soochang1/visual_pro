import sys
from PySide6.QtWidgets import ( QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout
)

class CustomDlg(QDialog): 
    def __init__(self, parent = None):
        super().__init__(parent) 

        self.setWindowTitle('Hello, QDialog')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons) # buttons에 해당하는 button객체

        self.button_box.accepted.connect(self.accept) #QDialog의 메서드를 slot으로
        self.button_box.rejected.connect(self.reject)    #QDialog의 메서드를 slot으로

        message = QLabel('Is something ok?')

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box) # QDialogButtonBox객체 추가.
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomDlg()
    window.show()
    app.exec()