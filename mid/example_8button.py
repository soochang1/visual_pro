import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QDialog, QWidget

class SubWidget(QDialog): 
    def __init__(self, index):
        super().__init__()
        self.setWindowTitle(f'SubWidget {index}')
        message = QLabel(f'SubWidget {index} is open.')
        layout = QVBoxLayout()
        layout.addWidget(message)
        self.setLayout(layout)

class MW(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SubWidget Launcher")
        self.buttons = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

        for i in range(8):
            button = QPushButton(f"Open SubWidget {i+1}")
            button.clicked.connect(lambda checked, i=i: self.button_clicked(i))
            layout.addWidget(button)
            self.buttons.append(button)

    def button_clicked(self, index):
        print("Button clicked:", index)
        subwidget = SubWidget(index+1)
        subwidget.exec_()  # 수정된 부분: QDialog의 exec_() 메서드를 사용하여 모달로 표시

#프로그램 실행.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec())
