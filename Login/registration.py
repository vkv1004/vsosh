import sqlite3
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QDialog


class UserRegistration(QDialog):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("../user_messages.db")
        self.cursor = self.conn.cursor()

        self.setWindowTitle('Окно регистрации')
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel('Логин:   ')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Пароль: ')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.password_repeat_label = QLabel('Повторите пароль: ')
        self.password_repeat_input = QLineEdit()
        self.password_repeat_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Регистрация')
        self.login_button.clicked.connect(self.registration)

        layout = QVBoxLayout()
        layout_login = QHBoxLayout()
        layout_password = QHBoxLayout()
        layout_password_repeat = QHBoxLayout()

        layout_login.addWidget(self.username_label)
        layout_login.addWidget(self.username_input)
        layout.addItem(layout_login)

        layout_password.addWidget(self.password_label)
        layout_password.addWidget(self.password_input)
        layout.addItem(layout_password)

        layout_password_repeat.addWidget(self.password_repeat_label)
        layout_password_repeat.addWidget(self.password_repeat_input)
        layout.addItem(layout_password_repeat)

        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def registration(self):
        login = self.username_input.text()
        password = self.password_input.text()
        password_repeat = self.password_repeat_input.text()
        if password == password_repeat:
            self.cursor.execute(f"INSERT INTO users (username, password) VALUES ('{login}', '{password}')")
            self.conn.commit()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Проверьте, что пароли совпадают")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def __del__(self):
        self.conn.close()
        
