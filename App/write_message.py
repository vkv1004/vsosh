import sqlite3

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QComboBox


class Write_message(QDialog):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("../../user_messages.db")
        self.cursor = self.conn.cursor()

        self.setWindowTitle('Пишем письма')

        self.recipient_label = QLabel('Кому написать:   ')
        users = self.cursor.execute(f"SELECT username FROM users")
        self.recipient = QComboBox()
        for rec in users:
            self.recipient.addItem(rec[0])
        self.recipient.setFont(QFont("Times", 16))

        self.message_label = QLabel('Что написать: ')
        self.message = QTextEdit()
        self.message.setFont(QFont("Times", 14))
        self.message.setObjectName("textEdit1")

        self.button = QPushButton('Отправить')
        self.button.setFont(QFont("Times", 16))
        self.button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout_recipient = QHBoxLayout()
        layout_message = QHBoxLayout()

        layout_recipient.addWidget(self.recipient_label)
        layout_recipient.addWidget(self.recipient)
        layout.addItem(layout_recipient)

        layout_message.addWidget(self.message_label)
        layout_message.addWidget(self.message)
        layout.addItem(layout_message)

        layout.addWidget(self.button)
        self.setLayout(layout)

    def send_message(self):
        messages = self.message.toPlainText() + "\n"
        self.cursor.execute(f"UPDATE users SET message = (message || '{messages}') WHERE username='{self.recipient.currentText()}'")
        self.conn.commit()
        self.close()

    def __del__(self):
        self.conn.close()
        
