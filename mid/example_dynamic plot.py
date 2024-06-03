import sys #Python 시스템 모듈을 가져옴
import random #무작위 수를 생성하기 위한 모듈

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)

from PySide6.QtCore import QTimer #하나는 clear and redraw용, 하나는 in-place용

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg #Matplotlib 그래픽을 QT위젯으로 표시하는 데 사용.

matplotlib.use('QtAgg') 

class MyCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, figsize =(5,5), dpi=100):

        self.fig, self.axes = plt.subplots(
            1,2,
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)

class MW(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('ex: dynamic plot')

        self.plt_canvas = MyCanvas(self, (5,10), 100)

        n_data = 10
        interval_ms = 10
        self.x_data0 = list(range(n_data))
        self.x_data1 = list(range(n_data)) 
        self.y_data0 = [random.randint(0,20) for i in range(n_data)]
        self.y_data1 = [random.randint(0,20) for i in range(n_data)]

        self.update_plot0()
        self.old_plot_ref = None
        self.update_plot1()   


        self.setCentralWidget(self.plt_canvas)
        self.show()

        self.timer0 = QTimer()
        self.timer0.setInterval(interval_ms) # milliseconds
        self.timer0.timeout.connect(self.update_plot0)
        self.timer0.start()


        self.timer1 = QTimer()
        self.timer1.setInterval(interval_ms) # milliseconds
        self.timer1.timeout.connect(self.update_plot1)
        self.timer1.start()

    def update_plot0(self):
        self.y_data0 = [ *self.y_data0[1:], random.randint(0,20)]
        self.plt_canvas.axes[0].cla() #완전 지우는 것.
        self.plt_canvas.axes[0].plot(self.x_data0, self.y_data0, label='method0')
        self.plt_canvas.axes[0].grid()
        self.plt_canvas.axes[0].legend(loc='upper right')
        self.plt_canvas.draw() # trigger the canvas to update and redraw

    def update_plot1(self):    
        self.y_data1 = [ *self.y_data1[1:], random.randint(0,20)]
        if self.old_plot_ref is not None:
            self.old_plot_ref.set_ydata(self.y_data1)
        else: 
            self.old_plot_ref = self.plt_canvas.axes[1].plot(
                self.x_data1, self.y_data1, 
                label='method1',
            )[0]
            self.plt_canvas.axes[1].grid()
            self.plt_canvas.axes[1].legend(loc='upper right')
        self.plt_canvas.draw()

#프로그램 실행.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())