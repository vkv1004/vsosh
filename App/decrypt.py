from App.ciphers.Vigenere import Vigenere
from App.ciphers.Caesar import Caesar
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QFont


class Decrypt(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            "background-color: {}".format('#ffffff'))

        u1 = QVBoxLayout(self)
        u2 = QHBoxLayout(self)
        u3 = QHBoxLayout(self)
        u4 = QHBoxLayout(self)

        self.cypher = QComboBox(self)
        self.cypher.addItem("Виженер")
        self.cypher.addItem("Цезарь")
        self.cypher.setFont(QFont("Times", 16))
        u1.addWidget(self.cypher, 1)

        u1.addLayout(u2, 2)
        u1.addLayout(u3, 3)
        u1.addLayout(u4, 4)

        self.label = QLabel(self)
        self.label.setText('Ключ:       ')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u2.addWidget(self.label, 0)

        self.key = QLineEdit(self)
        self.key.setText("")
        self.key.setFont(QFont("Times", 16))
        u2.addWidget(self.key, 1)

        self.label = QLabel(self)
        self.label.setText('''Шифро-
        текст:''')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u3.addWidget(self.label, 0)

        self.ciphertext = QTextEdit(self)
        self.ciphertext.setFont(QFont("Times", 14))
        self.ciphertext.setObjectName("textEdit1")
        u3.addWidget(self.ciphertext, 1)

        self.label = QLabel(self)
        self.label.setText('''Открытый
        текст:''')
        self.label.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))
        self.label.setFont(QFont("Times", 16))
        u4.addWidget(self.label, 0)

        self.plaintext = QTextEdit(self)
        self.plaintext.setEnabled(False)
        self.plaintext.setFont(QFont("Times", 14))
        self.plaintext.setObjectName("ciphertext")
        u4.addWidget(self.plaintext, 1)

        self.btn = QPushButton('Расшифровать', self)
        self.btn.resize(1100, 50)
        self.btn.clicked.connect(self.decryption)
        self.btn.setFont(QFont("Times", 16))
        u1.addWidget(self.btn, 5)

    def decryption(self):
        plaintext = self.ciphertext.toPlainText()
        key = self.key.text()
        self.plaintext.setEnabled(True)
        if self.cypher.currentText() == "Виженер":
            self.plaintext.setPlainText(Vigenere.decrypt(plaintext, key))
        elif self.cypher.currentText() == "Цезарь":
            if not key.isdigit():
                self.key.setText("Ключ должен быть числом")
            else:
                self.plaintext.setPlainText(Caesar.decrypt(plaintext, key))
                
