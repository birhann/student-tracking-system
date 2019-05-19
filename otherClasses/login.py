from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import sys
import pickle as pc

from design.Ui_login import Ui_Login
from otherClasses.sqlExecute import sqlExecute
from otherClasses.warning import warning
from otherClasses.register import register


class logIn(QDialog,Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.oldPos = self.pos()

        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        self.btn_newAccount.clicked.connect(self.newAccount)
        self.btn_sign.clicked.connect(self.signIn)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.giris_control=None
        #pickle
        try:
            with open('userPickles/lastlog.pc', 'rb') as file:
                log=pc.load(file)
                if len(log)>0:
                    self.remember_me.setChecked(True)
                    self.username.setText(log[0])
                    self.password.setText(log[1])
        except:
            pass



    def newAccount(self):
        register().exec_()


    def isReMember(self):
        if self.remember_me.isChecked():
            try:
                with open('userPickles/lastlog.pc', 'wb') as file:
                    pc.dump([self.username.text(), self.password.text()], file)
            except:
                pass
        else:
            try:
                with open('userPickles/lastlog.pc', 'wb') as file:
                    file.truncate()
            except:
                pass


    def signIn(self):
        if len(self.username.text())<6 or len(self.password.text())<6:
            warning("Kullanıcı Adınız veya Şifreniz 6 Karakterden Küçük Olamaz").exec_()
        else:
            sql=sqlExecute(self.username.text(),self.password.text())

            if sql.login():
                print("Login Successful")
                # database operation
                self.giris_control = True
                self.isReMember()
                self.close()
            else:
                warning("Kullanıcı Adı ('{}') veya\nŞifre ('{}') hatalı.".format(self.username.text(),self.password.text())).exec_()
                self.username.setText("")
                self.password.setText("")










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

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=logIn()
    win.show()
    sys.exit(app.exec())