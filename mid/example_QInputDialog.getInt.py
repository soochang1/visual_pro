import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QInputDialog)

class MW (QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        
        layout = QVBoxLayout()
        tmp = QWidget()
        tmp.setLayout(layout)
        
        self.l_buttons = ['getText', 'getMultilineText', ]
        for idx, c_str in enumerate(self.l_buttons):
            button0 = QPushButton(c_str)
            button0.clicked.connect(self.slot00)
            layout.addWidget(button0)

        self.ret_label = QLabel()
        layout.addWidget(self.ret_label)
        
        self.setCentralWidget(tmp)

       
        layout.addWidget(button0)
        layout.addWidget(self.ret_label)

        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)


    def slot00(self):
        print(self.sender())

        sender = self.sender()

        if sender == self.l_button[0]:
            ret_val, is_ok = QInputDialog.getInt(
                    self,
                    "Input Integer",
                    "Enter Your Int Value!",
                    0,
                    0, 100,
                    3,
                    )
        elif tmp_str == self.l_button[1]:
            ret_val, is_ok = QInputDialog.getMultiLineText(
                self,
                "Input Multi-Line Text!",
                "Enter Your Multi-Line"
            )
            if is_ok:
                self.ret_label.setText(f'{ret_int}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())
