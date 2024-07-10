from App.decrypt import Decrypt
from App.encrypt import Encrypt
from App.mailbox import Mailbox
from PyQt5 import Qt
from PyQt5.QtGui import QFont


class Application(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)
        self.setWindowTitle('Криптопочта')

        self.tab = Qt.QTabWidget()
        self.tab.setFont(QFont("Times", 16))
        self.setCentralWidget(self.tab)
        self.setGeometry(100, 100, 1200, 900)
        self.setStyleSheet(
            "background-color: {}".format('#c4d1ff'))

        self.btnOpen = Mailbox()
        self.tab.addTab(self.btnOpen, "Письма")

        self.btnEncrypt = Encrypt()
        self.tab.addTab(self.btnEncrypt, "Шифрование")

        self.btnOpen = Decrypt()
        self.tab.addTab(self.btnOpen, "Расшифрование")
        
