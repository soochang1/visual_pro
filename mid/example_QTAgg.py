import sys #명령행 인수, 표준 입출력, 환경 변수, 인터프리터 설정등을 다룰 수 있다.

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
)

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg,
                                               NavigationToolbar2QT,
)


matplotlib.use('QtAgg')

class MyCanvas(FigureCanvasQTAgg): #QWidget, FigureCanvasQTAgg의 sub class이다.

    def __init__(self, parent=None, figsize =(5,5), dpi=100): #출판물에 경우 dpi = 600정도, figsize= inch

        self.fig, self.axes = plt.subplots(
            1,2, #1행 2열
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig) #self.fig로 연결(뒤에 위치한 이유는 fig가 필요하기 때문이다.)

class MW(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('ex: matplotlib')

        plt_canvas = MyCanvas(self, (5,10), 100)
        plt_canvas.axes[0].plot([0,1,2,3,4], [10,13,20,30,15], label='line') #line 그래프
        plt_canvas.axes[1].scatter([0,1,2,3,4], [10,13,20,30,15], label='scatter') #scatter 그래프
        for a in plt_canvas.axes:
            a.legend() #범례
            a.grid() 
            
        toolbar = NavigationToolbar2QT(plt_canvas, self)
        
        lm = QVBoxLayout()
        lm.addWidget(toolbar)
        lm.addWidget(plt_canvas)
        
        tmp = QWidget()
        tmp.setLayout(lm)

        self.setCentralWidget(tmp)
        self.show()

#프로그램 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())