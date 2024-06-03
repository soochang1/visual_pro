import sys             #라이브러리와 모듈을 가져온다.
import PySide6.QtCore    
from PySide6.QtWidgets import (QApplication, QWidget, QLabel)


# define classes for this program

class MW(QWidget):  #MW class는 QWidget를 상속한 subclass이다.
                    #이 class의 객체(or instance)인 window는 사용자가 GUI program에서 보게되는 window에 해당한다.
                    #이는 위의 예제 코드로 만드는 GUI 프로그램에서 최상위 instance(객체)이며, GUI에서 사용되는 다른 Components를 포함하고 있다. 
                    
    def __init__(self):   
        """ Constructor for Main Window Class """
        super().__init__()      #super()는 부모 클래스(=super class)의 proxy object를 반환해주므로 이 예제에서는 MW class의 부모클래스인 QWidget에 대한 객체를 반환해준다.
        self.initialize_ui()

    def initialize_ui(self):    #GUI application을 초기화하는 메서드initialize_u()를 호출한다.
        """setup GUI application."""
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PySide")
        self.setup_main_wnd()
        self.show() # Display the window on the screen

    def setup_main_wnd(self):
        """setup the main window."""
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!')
        hello_label.move(150,90)

# ===============================
# Run the program
if __name__ == '__main__':
    
    print(PySide6.__version__)
    print(PySide6.QtCore)

    # Event Loop 등을 위한 QApplication instance 생성.
    app = QApplication(sys.argv)  
    # main window 생성 및 show 호출.
    window = MW()   
    # Event Loop 시작.
    sys.exit(app.exec())    
    
  