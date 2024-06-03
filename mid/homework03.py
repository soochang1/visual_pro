import sys
import psutil
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 창 크기 설정
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("System Monitor")

        # Matplotlib 플롯 생성
        self.figure, (self.ax1, self.ax2) = plt.subplots(2, 1)
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)
        
        #subplot 간의 간격 조정
        self.figure.subplots_adjust(hspace = 0.5)

        # CPU와 메모리 데이터 저장용 리스트
        self.cpu_data = []
        self.memory_data = []

        # 타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1초마다 업데이트

    def update_plot(self):
        # CPU 및 메모리 데이터 수집
        cpu_percent = psutil.cpu_percent(interval=1, percpu = True)
        #코어 사용량의 평균
        avg_cpu_percent = sum(cpu_percent) / len(cpu_percent) 
        memory_percent = psutil.virtual_memory().percent

        # 데이터 리스트에 추가
        self.cpu_data.append(avg_cpu_percent)
        self.memory_data.append(memory_percent)

        # 플롯 업데이트
        self.ax1.clear()
        self.ax1.plot(self.cpu_data, label='CPU (%)')
        self.ax1.set_title('CPU Usage')
        self.ax1.set_xlabel('Time (s)')
        self.ax1.set_ylabel('CPU Usage (%)')

        self.ax2.clear()
        self.ax2.plot(self.memory_data, label='Memory (%)')
        self.ax2.set_title('Memory Usage')
        self.ax2.set_xlabel('Time (s)')
        self.ax2.set_ylabel('Memory Usage (%)')

        # 플롯 적용
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())