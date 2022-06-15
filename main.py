from PyQt5.QtWidgets import QDialog, QApplication, QDesktopWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import sys

class MainScreen(QDialog):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("MainScreen.ui",self)
        self.back.clicked.connect(self.GoToStartScreen)

    def GoToStartScreen(self):
        StartScreenNav = StartScreen()
        widget.addWidget(StartScreenNav)
        widget.setCurrentIndex(widget.currentIndex() - 1)

class StartScreen(QDialog):
    def __init__(self):
        super(StartScreen, self).__init__()
        loadUi("StartScreen.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()

        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            widget.move(widget.pos() + event.pos() - self.offset)

        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        widget.offset = None
        super().mouseReleaseEvent(event)


    def GotoMainScreen(self):
        MainScreenNav = MainScreen()
        widget.addWidget(MainScreenNav)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Preencha todos os campos antes de continuar.")

        else:
            self.GotoMainScreen()

def main():
    try:
        app = QApplication(sys.argv)

        global widget
        widget = QtWidgets.QStackedWidget()
        widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        InitScreen = StartScreen()
        widget.addWidget(InitScreen)

        widget.setFixedHeight(800)
        widget.setFixedWidth(1200)


        widget.offset = None

        widget.move(QDesktopWidget().availableGeometry().center() - widget.frameGeometry().center())
        widget.show()

        sys.exit(app.exec_())

    except Exception as error:
        print(error)

if __name__ == '__main__':
   main()