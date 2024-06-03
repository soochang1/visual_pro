import sys, os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton)

class MW(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("비밀번호 입력")
        
        self.name_label = QLabel("이름:")
        self.name_entry = QLineEdit()
        
        self.password_label = QLabel("비밀번호:")
        self.password_entry = QLineEdit()
        self.password_entry.setMaxLength(10) #비밀번호를 10글자로 제한
        self.password_entry.setEchoMode(QLineEdit.Password) #비밀번호를 숨김
        self.password_entry.textChanged.connect(self.check_special_characters) #비밀번호 입력 필드의 텍스트가 변경될 때마다 check_special_characters함수 호출
        self.password_entry.textChanged.connect(self.check_password)  #비밀번호 입력 필드의 텍스트가 변경될 때마다 check_password함수 호출
        
        self.submit_button = QPushButton("제출")
        self.submit_button.setEnabled(False) #초기에 비활성화
        self.submit_button.clicked.connect(self.submit) #버튼 클릭시 submit함수 호출
        
        layout = QVBoxLayout() #여러 위젯을 세로로 배치하게 한다. (QHBoxlayout: 가로배치)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
        self.show()
            
    #비밀번호 확인과 비밀번호 일치 시 이름, 비밀번호를 출력하는 함수        
    def submit(self):
        if self.password_entry.text() == '1234567890': #비밀번호 설정
            print("이름:",self.name)
            print("비밀번호:",self.password) 
            print("비밀번호 일치!")
            QApplication.quit() #프로그램 종료
            
        else:
            print("비밀번호 불일치!")
            
    #비밀번호를 입력받는 함수        
    def check_password(self):
        self.name= self.name_entry.text()
        self.password = self.password_entry.text()
    
    #특수문자 확인하는 함수        
    def check_special_characters(self):
        special_characters = set("!@#$%^&*()_{}:|\"<>?[]',./\\")
        if any(char in special_characters for char in self.password_entry.text()):
            self.submit_button.setEnabled(False)
            
        else:
            self.submit_button.setEnabled(True)
        
 
 # 프로그램 실행      
if __name__ == "__main__":
    app = QApplication(sys.argv) #어플리케이션 객체를 생성
    wnd = MW()
    sys.exit(app.exec())
        

