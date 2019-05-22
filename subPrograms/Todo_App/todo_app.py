from mysql.connector import MySQLConnection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import time
import Ui_add_task, Ui_todo_App_main, Ui_sign_in, Ui_sign_up, Ui_update

konu=""

config = {'user': 'root', 'password': '', 'host': '127.0.0.1'}
username=""
title=""


class database():
    def run_execute(self,sorgu):
        connection = MySQLConnection(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sorgu)
        connection.commit()
        connection.close()

    def createDb(self):
        try:
            sorgu = "create database todoapp character set utf8 collate utf8_general_ci;"
            self.run_execute(sorgu)
            config['database'] = 'todoapp'
        except:
            config['database'] = 'todoapp'

    def createUsersTable(self):
        try:
            sorgu = "create table users(username VARCHAR(50),password VARCHAR(30));"
            self.run_execute(sorgu)
        except:
            pass

    def creatToDoTable(self):
        try:
            sorgu = "create table to_do(username VARCHAR(50),task_title VARCHAR(20),task VARCHAR(300),important_level VARCHAR(20), start_time VARCHAR(30),end_time VARCHAR(30),status VARCHAR(10));"
            self.run_execute(sorgu)
        except:
            pass

    def getUsers(self):
        connect = MySQLConnection(**config)
        cursor = connect.cursor()
        cursor.execute("select * from users")
        return cursor.fetchall()

    def get_data_of_theUser(self,username):

        connect = MySQLConnection(**config)
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM `to_do` WHERE username='{}'".format(username))
        return cursor.fetchall()

    def get_ner_user_of_theUser(self,username):
        connect = MySQLConnection(**config)
        cursor = connect.cursor()
        cursor.execute('SELECT "new_user" FROM `users` WHERE username="{}" '.format(username))
        return cursor.fetchall()
    def add_data_of_user(self,username,taskTitle,task,importantLevel,startTime,endTime,status):
        sorgu="INSERT INTO `to_do`(`username`, `task_title`, `task`, `important_level`, `start_time`, `end_time`, `status`) VALUES('{}','{}','{}','{}','{}','{}','{}');"
        connect = MySQLConnection(**config)
        cursor = connect.cursor()
        cursor.execute(sorgu.format(username,taskTitle,task,importantLevel,startTime,endTime,status))
        connect.commit()
        connect.close()



class signUp(QDialog, database, Ui_sign_up.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        database.createDb(self)
        database.createUsersTable(self)
        database.creatToDoTable(self)

        self.btn_signup.clicked.connect(self.register)

    def register(self):
        if self.txt_username.text()=="" or self.txt_password.text()=="":
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Lütfen Username ve Password alanlarını eksiksiz doldurun.")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        elif len(self.txt_username.text())<5 or len(self.txt_password.text())<5:
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Kullanıcı Adı Ve Şifre 5 karakterden küçük olamaz.")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            username=self.txt_username.text()
            password=self.txt_password.text()
            control=self.addUser(username,password)
            if control:
                error = QMessageBox()
                error.setIcon(QMessageBox.Information)
                error.setText("Kayıt İşlemi Başarıyla Gerçekleşmiştir.")
                error.setWindowTitle("Başarılı")
                error.exec_()
                self.txt_username.clear()
                self.txt_password.clear()
                time.sleep(0.5)
                self.close()
                time.sleep(1.2)
                sign_in.show()
                sign_in.txt_username.setText(username)
                sign_in.txt_password.setText(password)
            else:
                self.txt_username.clear()

    def addUser(self,username,password):
        exist_users=database.getUsers(self)
        for i in exist_users:
            if i[0]==username:
                error = QMessageBox()
                error.setIcon(QMessageBox.Warning)
                error.setText("'{}' adlı kullanıcı adı başka bir kullanıcı tarafından kullanılıyor. Lütfen başka bir kullanıcı adı girin.".format(username))
                error.setWindowTitle("Username")
                error.exec_()
                return False

        sorgu = "INSERT INTO `users` (`username`, `password`) VALUES ('{}', '{}');".format(username, password)
        database.run_execute(self, sorgu)
        return True

class signIn(QDialog, database, Ui_sign_in.Ui_Dialog):
    def __init__(self):
        super().__init__()
        database.createDb(self)
        database.createUsersTable(self)
        database.creatToDoTable(self)
        global first_login
        first_login=1


        self.control=None
        self.setupUi(self)
        self.create_account_link.openExternalLinks()
        self.create_account_link.setText("<a href='create-now'> Create Now </a>")
        self.create_account_link.linkActivated.connect(self.create_account)
        self.btn_signin.clicked.connect(self.signIn_as_user)

    def create_account(self):
        self.close()
        create_account= signUp()
        create_account.exec_()

    def signIn_as_user(self):
        if len(self.txt_username.text())<5 or len(self.txt_password.text())<5:
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Kullanıcı Adı Ve Şifre 5 karakterden küçük olamaz.")
            error.setWindowTitle("Eksik Alan")
            error.exec_()
        else:
            global username
            username=self.txt_username.text()
            password=self.txt_password.text()
            users=database.getUsers(self)
            for i in users:
                if i[0]==username and i[1]==password:
                    error = QMessageBox()
                    error.setIcon(QMessageBox.Information)
                    error.setText("Giriş Başarılı")
                    error.setWindowTitle("Başarılı")
                    error.exec_()
                    self.control=True
                    self.close()
                    global main,first_login
                    main=to_do_main()
                    main.exec_()

            if self.control!=True:
                error = QMessageBox()
                error.setIcon(QMessageBox.Critical)
                error.setText("Kullanıcı Adı Veya Parola Yanlış")
                error.setWindowTitle("Yanlış Girdi")
                error.exec_()
                time.sleep(0.4)
                self.txt_password.clear()
                self.txt_username.clear()
            self.control=None

class to_do_main(QDialog, database, Ui_todo_App_main.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_gorevEkle.clicked.connect(self.gorev_ekle)
        self.btn_gorev_sil.clicked.connect(self.gorev_sil)
        self.btn_tumunu_sil.clicked.connect(self.tumunu_sil)
        self.tv.doubleClicked.connect(self.edit1)
        self.tv2.doubleClicked.connect(self.edit2)
        self.tv3.doubleClicked.connect(self.edit3)


        self.model, self.model2, self.model3 = QStandardItemModel(), QStandardItemModel(), QStandardItemModel()
        self.gelecek_gorevler=[]
        self.gecmis_gorevler=[]
        self.log_control=0
        self.login_control()

    def login_control(self):
        # eski kullanıcının bilgilerini var olan modelden ve listeden temizleme
        print("modeller clear")
        self.model.clear()
        self.model2.clear()
        self.model3.clear()
        self.gelecek_gorevler.clear()
        self.gecmis_gorevler.clear()
        self.get_model()
        print("get model sonrası")
        self.data_exist() #kullanıcının hesabında veri olup olmamasına göre sil butonunu kontrol ediyoruz


    def get_model(self):
        global username
        #create models
        self.model.setHorizontalHeaderLabels(['Görev', 'Önem', 'Başlangıç','Bitiş','Durum'])
        self.model2.setHorizontalHeaderLabels(['Görev', 'Önem', 'Başlangıç','Bitiş','Durum'])
        self.model3.setHorizontalHeaderLabels(['Görev', 'Önem', 'Başlangıç','Bitiş','Durum'])
        self.info =database.get_data_of_theUser(self,username)
        global first_login
        if len(self.info)==0:
            if first_login!=1:
                info = QMessageBox()
                info.setIcon(QMessageBox.Information)
                info.setText("ToDo Listeniz Boş Görünüyor. Biraz Görev Eklemeye Ne Dersiniz? ")
                info.setWindowTitle("ToDo List")
                info.exec()
            first_login = 0
        else:
            #model 1 (Görevler)
            status_control=0
            for a in self.info:
                if a[6]=="true":
                    self.gelecek_gorevler.append(a)
                    self.model.appendRow([QStandardItem(a[1]), QStandardItem(a[3]), QStandardItem(a[4]), QStandardItem(a[5]),QStandardItem("Devam Ediyor")])
                    self.model.item(status_control, 4).setBackground(QColor(184,194,255))
                    status_control+=1
                else:
                    self.gecmis_gorevler.append(a)
                    self.model.appendRow([QStandardItem(a[1]), QStandardItem(a[3]), QStandardItem(a[4]), QStandardItem(a[5]),QStandardItem("Tamamlandı")])
                    self.model.item(status_control, 4). setBackground(QColor(243, 201, 202))
                    status_control += 1



            #model-2 (Gelecek Görevler) ve model-3 (Geçmiş Görevler)
            for i in self.gelecek_gorevler:
                self.model2.appendRow([QStandardItem(i[1]), QStandardItem(i[3]), QStandardItem(i[4]), QStandardItem(i[5]),QStandardItem("Devam Ediyor")])

            for i in self.gecmis_gorevler:
                self.model3.appendRow([QStandardItem(i[1]), QStandardItem(i[3]), QStandardItem(i[4]), QStandardItem(i[5]),QStandardItem("Tamamlandı")])

            #status-control
            for a in range(len(self.gelecek_gorevler)):
                self.model2.item(a, 4).setBackground(QColor(184,194,255))
            for a in range(len(self.gecmis_gorevler)):
                self.model3.item(a, 4).setBackground(QColor(243, 201, 202))
            self.tv.setModel(self.model),self.tv2.setModel(self.model2),self.tv3.setModel(self.model3)

            self.tv.setStyleSheet("font-size:23px")
            self.tv2.setStyleSheet("font-size:23px")
            self.tv3.setStyleSheet("font-size:23px")

            self.tv.resizeColumnsToContents()
            self.tv2.resizeColumnsToContents()
            self.tv3.resizeColumnsToContents()



    def gorev_ekle(self):
        task_add=add_task()
        task_add.exec_()
    def gorev_sil(self):
        try:
            self.index=self.tv.selectedIndexes()
            for index in self.index:
                title=index.sibling(index.row(),0).data()
            sorgu = "DELETE FROM `to_do` WHERE username='{}' and task_title='{}'".format(username,title)
            database.run_execute(self, sorgu)
            self.login_control()
        except:
            info = QMessageBox()
            info.setIcon(QMessageBox.Information)
            info.setText("Lütfen Bir Satır Seçin ")
            info.setWindowTitle("ToDo List")
            info.exec_()
    def tumunu_sil(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Tüm Veriyi Silmek İstediğinize Eminmisiniz")
        msgBox.setWindowTitle("Uyarı !")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue==msgBox.Ok:
            sorgu='DELETE FROM `to_do` WHERE username="{}"'.format(username)
            database.run_execute(self,sorgu)
            self.login_control()
        else:
            pass
    def data_exist(self):
        data_count=database.get_data_of_theUser(self,username)
        if len(data_count)<1:
            self.btn_gorev_sil.setEnabled(False)
            self.btn_tumunu_sil.setEnabled(False)
        else:
            self.btn_tumunu_sil.setEnabled(True)
            self.btn_gorev_sil.setEnabled(True)



    def edit1(self):
        self.edit(1)
    def edit2(self):
        self.edit(2)
    def edit3(self):
        self.edit(3)

    def edit(self,tableV):
        global title,status_update
        status_update=update_status()

        #secilen indexin titleını çekme
        if tableV==1:
            self.index = self.tv.selectedIndexes()
        elif tableV==2:
            self.index=self.tv2.selectedIndexes()
        else:
            self.index=self.tv3.selectedIndexes()

        for index in self.index:
            title = index.sibling(index.row(),0).data()
            print(title)

        #------------------------------

        #checkboxı veritabanındaki bilgiye göre seçili yapma veya yapmama işlemi
        connection = MySQLConnection(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT `status` FROM `to_do` WHERE username = '{}' AND task_title = '{}'".format(username, title))
        status_dict= cursor.fetchone()
        is_it_done=status_dict['status']
        if is_it_done=="true":
            status_update.radio_devam_ediyor.setChecked(True)

        else:
            status_update.radio_tamalandi.setChecked(True)
        #----------------------------------------------------------------------

        #veritabanından konu içeriğini alıp PlainTexte yerleştirme işlemi
        connection2 = MySQLConnection(**config)
        cursor2 = connection2.cursor(dictionary=True)
        cursor2.execute("SELECT `task` FROM `to_do` WHERE username = '{}' AND task_title = '{}'".format(username, title))
        task=cursor2.fetchone()
        status_update.txt_detail.setPlainText(task['task'])
        #----------------------------------------------------------------
        status_update.exec_()

class add_task(QDialog, database, Ui_add_task.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ekle.clicked.connect(self.addTask)

    def addTask(self):
        global username
        taskTitle = self.txt_task_title.text().upper()
        taskDetail = self.txt_task_detail.toPlainText()
        importantLevel = self.important_level.currentText()
        startTime = self.start_time.text()
        endTime = self.end_time.text()
        status="true"

        #aynı başlıkla başka bir konu var mı?
        connection = MySQLConnection(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM `to_do` WHERE username='{}' AND task_title='{}'".format(username, taskTitle))
        isHave = cursor.fetchall()
        if len(isHave) > 0:
            info = QMessageBox()
            info.setIcon(QMessageBox.Warning)
            info.setText("Aynı Başlığa Sahip Birden Fazla Konu Ekleyemezsiniz. Lütfen Farklı Bir İsim Deneyin")
            info.setWindowTitle("ToDo List")
            info.exec_()

        else:
            print(username,taskTitle,taskDetail,importantLevel,startTime,endTime,status)
            database.add_data_of_user(self, username,taskTitle,taskDetail,importantLevel,startTime,endTime,status)

            self.close()
            global main
            main.login_control()

            time.sleep(0.2)

            self.veri=database.get_data_of_theUser(self,username)
            if len(self.veri)==1:
                info = QMessageBox()
                info.setIcon(QMessageBox.Information)
                info.setText("Görev Durumunda Değişiklik Yapmak İçin Görevin Bulunduğu Satıra Çift Tıklayabilirsiniz.")
                info.setWindowTitle("ToDo List")
                info.exec_()
class update_status(QDialog, database, Ui_update.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_guncelle.clicked.connect(self.change_status)

    def change_status(self):
        global title,konu
        connection = MySQLConnection(**config)
        cursor = connection.cursor(dictionary=True)
        if self.radio_devam_ediyor.isChecked(): #devam ediyor checkboı seçili ise durumu true olarak güncelle
            cursor.execute("UPDATE `to_do` SET `status`='true' WHERE username = '{}' and task_title = '{}'".format(username,title))
            connection.commit()
            connection.close()
        else: # durumu true olarak güncelle
            cursor.execute("UPDATE `to_do` SET `status`='false' WHERE username = '{}' and task_title = '{}'".format(username,title))
            connection.commit()
            connection.close()

        main.login_control()
        self.close()

if __name__=="__main__":
    main=object
    task_add=object
    status_update=object
    first_login=1
    index=""

    toDoapp=QApplication(sys.argv)
    sign_in=signIn()
    sign_in.show()
    sys.exit(toDoapp.exec_())


