import sys, os #system(파이썬 인터프리터)과 관련된 것들을 처리, os = operation과 관련된 것들을 처리
from datetime import datetime #시간을 측정하기 위해서

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QStatusBar,
    QLabel,
    QProgressBar,
    QPushButton,
)

from PySide6.QtCore import QTimer #내부적으로 시계를 돌려서 매 초마다 timeout이 발생하면 event가 발생하도록하는 장치


class MW(QMainWindow):

    def __init__(self):

        super(MW, self).__init__()

        # set status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # set timer to display time by permanent widget
        self.timer0 = QTimer(self)
        self.timer0.timeout.connect(self.update_clk)
        self.timer0.start(1000) # 1 sec = 1000 ms

        # permanent widget: clock
        self.clk_label = QLabel()
        self.status_bar.addPermanentWidget(self.clk_label) #permant = 영구적인

        # temporary widget: progressbar
        self.progress_bar = QProgressBar(self, minimum=0, maximum =100)
        self.status_bar.addWidget(self.progress_bar, 1) #2, 3으로 변경해볼것.

        # start button for progressbar
        self.btn = QPushButton('Start Progress!')
        self.btn.clicked.connect(self.start_progress)
        self.setCentralWidget(self.btn) #버튼을 직접 추가

        # timer for progressbar
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update_progress)
        self.progress_value = 0

        self.show()

    def start_progress(self): #상태바 구성
        self.progress_value = 0
        self.progress_bar.reset()
        self.progress_bar.setValue(self.progress_value)
        self.timer1.start(100)
        self.status_bar.showMessage('Progress started...', 2000)

    def update_clk(self):
        now = datetime.now()
        now_str = now.strftime('%H:%M:%S') #문자열로
        self.clk_label.setText(now_str) 

        # current_time = QTime.currentTime()

    def update_progress(self): #timer1 = 100이 되면 stop.
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer1.stop()
            self.status_bar.showMessage('Progress completed...', 2000)

#프로그램 실행
if __name__ == '__main__': #main에서 실행된다면
    app = QApplication(sys.argv) 
    wnd = MW()
    sys.exit(app.exec()) #exec가 끝나면 종료시킨다.
