from PySide2.QtWidgets import (QApplication, QMainWindow)
from graphic_design_2 import Ui_MainWindow
import sys
from quo import btn_quo
from oi import btn_oi
from zxml import btn_xml
from discount import btn_discount
from copy35 import btn_copy
from tempcopy import btn_temporary


def send_to_quo(w,a):
    btn_quo(w,a)

def send_to_oi(e,s):
    btn_oi(e,s)

def send_to_xml(r,d):
    btn_xml(r,d)

def send_to_multi(t,f):
    btn_quo(t,f)
    btn_oi(t,f)
    btn_xml(t,f)

def send_to_discount(u,h):
    btn_discount(u,h)

def send_to_copy(j):
    btn_copy(j)

def send_to_temporary(y):
    btn_temporary(y)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SAP Assistant")
        self.pushButton.clicked.connect(lambda: (send_to_quo(self.textEdit_2.toPlainText().split(), self.textEdit.toPlainText())))
        self.pushButton_2.clicked.connect(lambda: (send_to_oi(self.textEdit_2.toPlainText().split(), self.textEdit.toPlainText())))
        self.pushButton_3.clicked.connect(lambda: (send_to_xml(self.textEdit_2.toPlainText().split(), self.textEdit.toPlainText())))
        self.pushButton_4.clicked.connect(lambda: (send_to_multi(self.textEdit_2.toPlainText().split(), self.textEdit.toPlainText())))
        self.pushButton_5.clicked.connect(lambda: (send_to_discount(self.textEdit_2.toPlainText().split(), self.textEdit_3.toPlainText())))
        self.pushButton_6.clicked.connect(lambda: (send_to_copy(self.textEdit_2.toPlainText().split())))
        self.pushButton_7.clicked.connect(lambda: (send_to_temporary(self.textEdit_2.toPlainText().split())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()