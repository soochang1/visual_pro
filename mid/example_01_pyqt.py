import PyQt6.QtCore
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel)  

import sys


class MW(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PyQt")
        #self.setup_main_wnd()
        
        # hello_label = QLabel(self)
        # hello_label.setText('Hello, World and Qt!')
        # hello_label.move(150,90)
        
        self.show() #화면에 ;창을 띄운다.
        
# class Qwidget(object):
    # def __init__(self):ac
        
    # def show(self):
        
        
if __name__ == "__main__":
   # app = QApplication(sys.argv) #항상 넣어주는 코드
    # main window 생성 및 show 호출.
    window = MW()  #window= 인스턴스(붕어빵), mw= 클래스(붕어빵틀)
    # Event Loop 시작.
    #sys.exit(app.exec())  #exec로 호출(사용자가 하는 모든 행동을 수신하려고 대기) return 값이 0이면 정상 종료, 항상 넣어주는 코드
    # sys.exit(0)와 같다.
    

#must cinstruct a QApplication before a Qwidget
app = QApplication(sys.argv)
window=MW()
sys,exit(app.exec())
