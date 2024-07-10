import sys
from App.application import Application
from Login.authorization import UserAuthentication
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = UserAuthentication()
    login.show()
    login.exec_()
    if login.Accepted:
        ap = Application()
        ap.show()
    app.exec_()
    
