import os
from App.write_message import Write_message
import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QFont


class Mailbox(QWidget):
    def __init__(self):
        super().__init__()
        file = open("id.txt", 'r')
        a = file.read()
        self.id = int(a)
        file.close()
        os.remove("id.txt")
        self.conn = sqlite3.connect("../../user_messages.db")
        self.cursor = self.conn.cursor()
        self.setStyleSheet(
            "background-color: {}".format('#ffffff'))

        u1 = QVBoxLayout(self)

        self.label = QLabel(self)
        self.label.setText('Письма:')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u1.addWidget(self.label, 1)

        self.plaintext = QTextEdit(self)
        self.plaintext.setFont(QFont("Times", 14))
        self.plaintext.setObjectName("textEdit1")
        messages = self.cursor.execute(f"SELECT message FROM users WHERE id='{self.id}'")
        array_messages = ""
        for message in messages:
            if message[0]:
                array_messages = message[0].replace(r"\n", "\n") + "\n"
        self.plaintext.setPlainText(array_messages)
        u1.addWidget(self.plaintext, 2)

        self.btn = QPushButton('Написать сообщение', self)
        self.btn.resize(1100, 50)
        self.btn.clicked.connect(self.write)
        self.btn.setFont(QFont("Times", 16))
        u1.addWidget(self.btn, 3)

    def write(self):
        f = Write_message()
        f.show()
        f.exec_()
        
