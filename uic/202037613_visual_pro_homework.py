import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTextEdit, QVBoxLayout, QWidget

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('간단한 텍스트 편집기')
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()
        self.createStatusBar()

    def createMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('파일')
        open_action = QAction('열기', self)
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

        edit_menu = menubar.addMenu('편집')
        save_action = QAction('저장', self)
        save_action.triggered.connect(self.saveFile)
        edit_menu.addAction(save_action)

    def createStatusBar(self):
        self.statusBar().showMessage('Ready')

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, '파일 선택', '.', '텍스트 파일 (*.txt)')

        if filename:
            with open(filename, 'r') as f:
                self.text_edit.setText(f.read())

    def saveFile(self):
        text = self.text_edit.toPlainText()
        filename, _ = QFileDialog.getSaveFileName(self, '파일 저장', '.', '텍스트 파일 (*.txt)')

        if filename:
            with open(filename, 'w') as f:
                f.write(text)
                self.statusBar().showMessage(f'저장됨: {filename}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
