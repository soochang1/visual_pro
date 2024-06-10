import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget,
    QListWidgetItem, 
    QHBoxLayout, QVBoxLayout, QWidget, QFileDialog, QMenuBar, 
    QStatusBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.image as mpimg

class ImageCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.setStyleSheet("background-color: #2f2f2f;")
        self.ax.axis('off')  # Hide the axis
        self.fig.subplots_adjust(
            left=0, right=1,
            top=1, bottom=0
        )

    def display_image(self, image_path):
        self.ax.clear()
        img = mpimg.imread(image_path)
        self.ax.imshow(img)
        self.ax.axis('off')  # Hide the axis
        self.fig.subplots_adjust(
            left=0, right=1,
            top=1, bottom=0
        )
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JPG Viewer")

        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        right_layout = QVBoxLayout()
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        
        # 마우스 클릭 및 더블클릭 이벤트 연결
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        
        #마우스 드래그 상태 및 사각형 선택을 위한 변수 초기화
        self.dragging = False
        self.rect = None
        self.start_point = (0,0)
        self.click_count = 0

        # QListWidget 생성 및 설정
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        main_layout.addWidget(self.list_widget)
        
        
        # Matplotlib FigureCanvas 생성 및 설정
        self.canvas = ImageCanvas(self)
        
        # NavigationToolbar 생성 및 설정.
        self.nav_toolbar = NavigationToolbar(self.canvas, self)
        
        right_layout.addWidget(self.nav_toolbar)
        right_layout.addWidget(self.canvas)
        
        
        main_layout.addWidget(right_widget)

        # StatusBar 생성
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # 메뉴바 설정
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Select Img Dir")
        menubar.setNativeMenuBar(False)

        # 디렉토리 선택 액션 추가
        open_action = QAction("Open Directory", self)
        open_action.triggered.connect(self.open_directory)
        file_menu.addAction(open_action)
    
        self.show()
        
    def on_click(self, event):
        if self.image is None:
            return
        
        if event.button == 3:
            self.on_right_click(event)
        else:
            if event.inaxes != self.ax:
                return
            self.dragging = True
            self.start_point = (event.xdata, event.ydata)
            self.rect = self.ax.add_patch(
                plt.Rectangle(self.
                              start_point, 
                              0, 0, 
                              fill=False, color='red')
                )
            self.canvas.draw()
                
                

    def open_directory(self):
        # 디렉토리 선택 다이얼로그 열기
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.list_widget.clear()
            # 디렉토리의 png 파일 목록 가져오기
            jpg_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
            for jpg_file in jpg_files:
                item = QListWidgetItem(jpg_file)
                item.setData(Qt.UserRole, os.path.join(directory, jpg_file))
                self.list_widget.addItem(item)

    def on_item_clicked(self, item):
        # 선택된 아이템의 파일 경로를 가져와서 이미지 표시
        file_path = item.data(Qt.UserRole)
        self.canvas.display_image(file_path)
        self.status_bar.showMessage(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())