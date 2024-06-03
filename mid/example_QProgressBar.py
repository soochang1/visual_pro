import sys #파이썬에서 돌아가는 프로세스와 상호작용하는 모듈

from PySide6.QtWidgets import(
    QApplication, #이벤트 루프가 돌아가게 한다.
    QMainWindow, 
    QProgressBar, 
    QPushButton, 
    QWidget, QVBoxLayout,
)
from PySide6.QtCore import QTimer #QTimer: 어떤 인터벌 간격으로 타임아웃 시그널을 보내는 녀석

class MW(QMainWindow):  #MW클래스는 QMAinWindow를 상속하며, PySide6 애플리케이션의 main window에 해당

    def __init__(self): 
        super(MW, self).__init__() #부모클래스(MW)를 재사용하는 녀석. 
        self.setWindowTitle("ex: QProgressBar") 
        self.setGeometry(200, 200, 300, 150)

        self.progressBar = QProgressBar(self, minimum=9, maximum=20) 
        self.progressValue = self.progressBar.minimum()
        #self.progressBar.setGeometry(50, 50, 200, 30)

        self.startButton = QPushButton("start", self)
        #self.startButton.setGeometry(100, 100, 100, 30)
        self.startButton.clicked.connect(self.startProgress)

        self.timer = QTimer(self) #계속해서 인스턴스 어트리뷰트로 작동, 하지만 self를 제거할시 해당하는 메소드가 끝나면 사라짐.
        self.timer.timeout.connect(self.updateProgress)
        self.progressValue = 0

        lm = QVBoxLayout()
        lm.addWidget(self.progressBar)
        lm.addWidget(self.startButton)

        tmp = QWidget()
        tmp.setLayout(lm)

        self.setCentralWidget(tmp)
        self.show()

    def startProgress(self):
        self.progressBar.reset()
        self.progressValue = self.progressBar.value()
        self.startButton.setEnabled(False)
        # self.progressBar.setValue(self.progressValue)
        self.timer.start(100)  # 100 milliseconds마다 타이머 발생

    def updateProgress(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
        if self.progressValue >= self.progressBar.maximum():
            self.timer.stop()
            #self.progressBar.reset()
            self.startButton.setEnabled(True)


#프로그램 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())
    
    