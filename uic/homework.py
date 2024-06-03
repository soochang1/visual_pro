import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtGui import QIcon, QAction
from ui_design import Ui_MainWindow 
class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.initUI()

    def initUI(self):
        loadUIAction = QAction('Load UI', self)
        loadUIAction.setShortcut('Ctrl+L')
        loadUIAction.setStatusTip('Load UI from ui_design.py')
        loadUIAction.triggered.connect(self.loadUI)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(loadUIAction)
        
        editmenu = menubar.addMenu('&Edit')
        
        cutAction = QAction(QIcon(), 'Cut', self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.setStatusTip('Cut text')
        cutAction.triggered.connect(self.cutText)
        editmenu.addAction(cutAction)

        copyAction = QAction(QIcon(), 'Copy', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.setStatusTip('Copy text')
        copyAction.triggered.connect(self.copyText)
        editmenu.addAction(copyAction)

        pasteAction = QAction(QIcon(), 'Paste', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.setStatusTip('Paste text')
        pasteAction.triggered.connect(self.pasteText)
        editmenu.addAction(pasteAction)

        undoAction = QAction(QIcon(), 'Undo', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.setStatusTip('Undo last action')
        undoAction.triggered.connect(self.undoText)
        editmenu.addAction(undoAction)

        redoAction = QAction(QIcon(), 'Redo', self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.setStatusTip('Redo last action')
        redoAction.triggered.connect(self.redoText)
        editmenu.addAction(redoAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def loadUI(self):
        self.ui.setupUi(self)
        self.ui.textEdit.textChanged.connect(self.countCharacters)

    def countCharacters(self):
        text = self.ui.textEdit.toPlainText()
        char_count = len(text)
        self.statusBar().showMessage(f'Character count: {char_count}')

    def cutText(self):
        self.ui.textEdit.cut()

    def copyText(self):
        self.ui.textEdit.copy()

    def pasteText(self):
        self.ui.textEdit.paste()

    def undoText(self):
        self.ui.textEdit.undo()

    def redoText(self):
        self.ui.textEdit.redo()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
