import time

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import sys


from otherClasses.send_email import sendMail as mail
from otherClasses.warning import warning
from otherClasses.sqlExecute import sqlExecute
from design.Ui_register import Ui_Register

class register(QDialog,Ui_Register):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.oldPos = self.pos()
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_createAccount.clicked.connect(self.createAccount)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.db_data={}
        self.error_msg=[]
        self.login=True


    def createAccount(self):
        self.db_data={
            'ad':self.name.text(),
            'soyad':self.surname.text(),
            'kullaniciAdi':self.username.text(),
            'sifre':self.password.text(),
            'ePosta': self.e_mail.text(),
            'bolumAdi':self.department_name.text()
        }
        #is there any empty field
        if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [self.db_data[i] for i in self.db_data].count('')>0 else False) is not False:return
        #name and surname field can`t be empty
        self.error_msg="Ad ve Soyad Alanını En Az 2 Karakter Olmalıdır"
        if (warning(self.error_msg).exec_() if len(self.db_data['ad'])<2 or len(self.db_data['soyad'])<2else False) is not False:return
        #username field length cant`t be lower than 6
        self.error_msg="Kullanıcı Adı En Az Altı Karakter Olmalıdır"
        if (warning(self.error_msg).exec_() if len(self.db_data['kullaniciAdi']) < 6 else False) is not False: return
        #e_mail is a real e-mail??
        self.error_msg="Lütfen Geçerli Bir E-Posta Adresi Giriniz"
        if (warning(self.error_msg).exec_() if self.db_data['ePosta'].count('@')==0 or self.db_data['ePosta'].count('.com')==0else False) is not False :return
        #is have lowwecase and uppercase and numeric??
        self.error_msg="Lütfen Şifrenizde Büyük-Küçük Harf ve Rakam Kullanınız"
        if (warning(self.error_msg).exec_() if ([i.isupper() for i in self.db_data['sifre']].count(True) <1 or [i.islower() for i in self.db_data['sifre']].count(True) <1 or [i.isalpha() for i in self.db_data['sifre']].count(False) < 1) else False) is not False : return

        #to sent mail register info
        if self.sent_account_info.isChecked():
            body="""
            Merhaba %s %s Hesap Bilgileriniz Aşağıdaki Gibidir, Mutlu Günler Dileriz.<br><br>
            Kullanıcı Adınız:'%s'<br>
            Şifreniz: '%s'<br>
            Bölüm Adınız: %s
            """%(self.db_data["ad"],self.db_data['soyad'],self.db_data['kullaniciAdi'],self.db_data['sifre'],self.db_data['bolumAdi'])
            mail([self.db_data['ePosta']],"ÖTS Bilgilendirme",body)


        #REGISTER
        sql=sqlExecute(self.username.text(),self.password.text())
        sql.register(self.db_data)
        time.sleep(0.8)
        self.close()







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
    win=register()
    win.show()
    sys.exit(app.exec())


