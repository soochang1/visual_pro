from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont,QPixmap
from PySide6.QtCore import Qt 

import os
import sys

class main_wnd(QWidget):
    def __init__(self):
         super().__init__()
         
         #main window의 크기를 설정
         self.setGeometry(100,20,600,300)
         self.setFixedSize(600,300)
         
         self.ds_set_mwd()
        
         self.show()
         
         
    def ds_set_mwd(self):
         label0=QLabel('Hello, World!',self)
         label0.setFont(QFont('Arial',20))
         label0.setStyleSheet('background-color: red')
         label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
         label0.move(30,30)
         
         self.ds_set_label1()
         
    def ds_set_label1(self):
        label1 = QLabel(self)
        
        fstr=os.path.realpath(__file__)
        pstr=os.path.dirname(fstr)
        istr=os.path.join(pstr, 'c:/visual_pro/test_image/blue.jpg')
        pixmap= QPixmap('/test_image/blue.JPG')
        label1.setPixmap(pixmap)
        
        label1.move(30,30)
         
    
if __name__=='__main__':
     app=QApplication(sys.argv)
    
     mw=main_wnd()
    
     sys.exit(app.exec()) 
     