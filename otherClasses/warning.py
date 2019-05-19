from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import sys

from design.Ui_warning import Ui_warning

class warning(QDialog,Ui_warning):
    def __init__(self,error_msg):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(self.close)
        self.btn_tamam.clicked.connect(self.close)
        self.oldPos=self.pos()
        self.error_msg=error_msg
        self.txt_error.setPlainText(self.error_msg)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    def exit(self):
        sys.exit()


if __name__=="__main__":
    app=QApplication(sys.argv)
    win=warning("Deneme")
    win.show()
    sys.exit(app.exec())