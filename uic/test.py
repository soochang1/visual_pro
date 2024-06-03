from PySide6.QtWidgets import QMainWindow, QApplication
import sys

# outputfile.py가 변환된 python code파일.
# Ui_MainWindow가 Qt Designer로 만들어진 widget class
from output import Ui_MainWindow 

class MyWindow(QMainWindow, Ui_MainWindow): # 중복으로 상속.
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 반드시 호출
        self.lineEdit.returnPressed.connect(self.my_slot)
        self.show()
        
    def my_slot(self):
        c_text = self.lineEdit.text()
        self.label.setText(c_text)
             
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
    