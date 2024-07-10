import sqlite3
from Login.registration import UserRegistration
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class UserAuthentication(QDialog):
    mysignal = QtCore.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("../user_messages.db")
        self.cursor = self.conn.cursor()
        self.user_name = ""

        self.setWindowTitle('Окно авторизации')
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel('Логин:   ')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Пароль: ')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Авторизация')
        self.login_button.clicked.connect(self.login)

        self.registration_button = QPushButton('Регистрация')
        self.registration_button.clicked.connect(self.registration)

        layout = QVBoxLayout()
        layout_login = QHBoxLayout()
        layout_password = QHBoxLayout()
        layout_login.addWidget(self.username_label)
        layout_login.addWidget(self.username_input)
        layout.addItem(layout_login)
        layout_password.addWidget(self.password_label)
        layout_password.addWidget(self.password_input)
        layout.addItem(layout_password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.registration_button)
        self.setLayout(layout)

    def login(self):
        login = self.username_input.text()
        password = self.password_input.text()
        self.cursor.execute(f"SELECT id FROM users WHERE username='{login}' AND password='{password}'")
        flag = self.cursor.fetchone()
        if flag:
            file = open("id.txt", 'w')
            file.write(str(flag)[1:-2])
            file.close()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Введены несуществующие данные")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def registration(self):
        self.registration_window = UserRegistration()
        self.registration_window.show()
        self.registration_window.exec_()
        
