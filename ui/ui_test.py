from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class MyApp(QWidget): #상속 받기
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("test.ui")
        self.ui.btn_01.clicked.connect(self.show_msg) # 메세지를 호출
        self.ui.show()

    def show_msg(self):
        print("test")


if __name__ == '__main__':
    app = QApplication([])
    w = MyApp()
    app.exec_()

