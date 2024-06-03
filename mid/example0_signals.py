import sys
import traceback

PYSIDE = True
try:
    from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton)

except:
    e_msg=traceback.format_exc()
    print(e_msg) 
    PYSIDE = False
    
class MW(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Ex: QCheckbox")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        lm=QVBoxLayout()
        
        lm.addWidget(QLabel('What is most important?')) 
        
        self.le = QLineEdit()
        self.le.setMaxLength(10) # 10글자 제한.
        self.le.returnPressed.connect(self.on_return_pressed)
        self.le.textChanged.connect(self.on_changed)
        self.le.textEdited.connect(self.on_edited)
        self.le.editingFinished.connect(self.on_editing_finished)
        lm.addWidget(self.le)

        self.dp_label0 = QLabel()
        lm.addWidget(self.dp_label0)
        self.dp_label1 = QLabel()
        lm.addWidget(self.dp_label1)
        self.dp_label2 = QLabel()
        lm.addWidget(self.dp_label2)

        self.dp_label3 = QLabel()
        lm.addWidget(self.dp_label3)
        self.le.textChanged.connect(self.dp_label3.setText)        

        self.setLayout(lm)  
        
    def on_return_pressed(self):
        tmp = self.le.selectedText()
        print(f'selected text:{tmp}')

    def on_changed(self, text):
        tmp = "textChanged:"
        tmp += text 
        self.dp_label0.setText(tmp)

    def on_edited(self, text):
        tmp = "textEdited:"
        tmp += text 
        self.dp_label1.setText(tmp)

    def on_editing_finished(self):
        tmp = "editingFinished"
        tmp += self.le.text() 
        self.dp_label2.setText(tmp)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    main_wnd = MW()
    sys.exit(app.exec())   #이 친구가 return이 되는 순간까지 창을 유지하는 역할
    