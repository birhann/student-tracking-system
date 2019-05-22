from otherClasses.login import logIn
from otherClasses.warning import warning
from otherClasses.sqlExecute import sqlExecute
from design.Ui_ogrenciTakip import Ui_MainWindow



import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *


class ogrenciTakip(QMainWindow,Ui_MainWindow):
    def __init__(self):
        login=logIn()
        login.exec_()
        super().__init__()
        self.setupUi(self)
        self.oldPos=self.pos()

        #USER INFO
        self.username=login.username.text()
        self.password=login.password.text()
        self.userInfo = {}

        # MENU BAR AND TOOL BAR
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        # DROP - DOWN
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # LOGIN
        if login.giris_control is None:
            sys.exit()
        else:
            # MENU - LEFT SIDE
            self.menuStack.hide()
            self.btn_profil.clicked.connect(self.showWidget)
            self.btn_ders.clicked.connect(self.showWidget)
            self.btn_ogrenci.clicked.connect(self.showWidget)
            self.btn_yoklama_not.clicked.connect(self.showWidget)
            self.btn_ogrenci_ekle.clicked.connect(self.showWidget)
            self.btn_ogrenci_duzenle.clicked.connect(self.showWidget)
            self.btn_ogrenci_goruntule.clicked.connect(self.showWidget)
            self.btn_ders_ekle.clicked.connect(self.showWidget)
            self.btn_ders_duzenle.clicked.connect(self.showWidget)
            self.btn_ders_goruntule.clicked.connect(self.showWidget)
            self.btn_not_gir.clicked.connect(self.showWidget)
            self.btn_yoklama_al.clicked.connect(self.showWidget)
            self.open_close_control="close"
            self.last_menu = ["profil"]
            self.opened_menu=[self.btn_profil]



            # MENU TOP - RIGHT SIDE
            self.hesapWidget.hide()
            self.btn_hesap.clicked.connect(self.showWidget)
            self.btn_hesap_setting.clicked.connect(self.showWidget)


            # CONNECT DATABASE AND GET INFO - SET INFO TO WIDGETS
            self.connectDatabase()
            self.setInfo()


            ##### FOR MAİN OPERATIONS ####
            # for students
            self.combo_edit_learners.activated.connect(self.ogrenciSection)
            self.combo_yerlestir_classes.activated.connect(self.ogrenciSection)
            self.combo_yerlestir_learners.activated.connect(self.ogrenciSection)
            self.btn_ogrenciEkle.clicked.connect(self.ogrenciSection)
            self.btn_ogrenciDuzenle.clicked.connect(self.ogrenciSection)
            self.btn_ogrenciSil.clicked.connect(self.ogrenciSection)
            self.btn_ogrenciBilgileriGetir.clicked.connect(self.ogrenciSection)
            self.btn_ogrenciYerlestir.clicked.connect(self.ogrenciSection)
            self.btn_ogrenciDersKaydi.clicked.connect(self.ogrenciSection)

            self.label_yerlestir_class.hide()
            self.label_yerlestir_learners.hide()
            # for lessons
            self.btn_dersEkle.clicked.connect(self.dersSinifSection)
            self.btn_sinifEkle.clicked.connect(self.dersSinifSection)


    def connectDatabase(self):
        self.sql=sqlExecute(self.username,self.password)
        self.sql.config['database']='%s'%(self.username)
        info=self.sql.getUserInfo()
        self.userInfo ={
            'name':info[0]['name'],
            'surname':info[0]['surname'],
            'e_mail':info[0]['e_mail'],
            'dp_no':info[0]['department_no'],
            'user_type':info[0]['user_type'],
        }

    def setInfo(self):
        self.ogr_duzenle_show_hide = [self.ogr_edit_ad, self.ogr_edit_soyad, self.ogr_edit_cinsiyet,self.ogr_edit_dogumTarihi, self.ogr_edit_evAdresi, self.ogr_edit_mail,self.ogr_edit_telefon]

        #ogrenci düzenle bölümü güncelleme
        def setClassEditInfo():
            classData = self.sql.getClassesInfo()
            self.combo_edit_classes.clear()
            self.combo_edit_classes.addItems(classData['code_name'])
            [i.hide for i in self.ogr_duzenle_show_hide]

        def setLearnerEditInfo():
            learnerData=self.sql.getLearnersInfo()
            self.combo_edit_learners.clear()
            self.combo_edit_learners.addItems(learnerData['name_and_surname'])
            [i.hide for i in self.ogr_duzenle_show_hide]

        #ogrenci ders-sınıf kaydı bölümü güncelleme
        def setLessondEditInfo():
            lessonData=self.sql.getLessonsInfo()
        def setClassesToEmplace():
            classData = self.sql.getClassesInfo()
            self.combo_yerlestir_classes.clear()
            self.combo_yerlestir_classes.addItems(classData['code_name'])
        def setLearnerToEmplace():
            studentsData=self.sql.getLearnersInNoClass()
            self.combo_yerlestir_learners.clear()
            self.combo_yerlestir_learners.addItems(studentsData)



        setLearnerToEmplace()
        setClassesToEmplace()
        setLearnerEditInfo()
        setClassEditInfo()

        self.label_username.setText("@"+self.username)
        self.label_department_name.setText(self.userInfo['dp_no']+" bölümü")

    def ogrenciSection(self):
        def ogrenciEkle():
            learnerData = {
                'ad': self.ogr_ekle_ad.text(),
                'soyad': self.ogr_ekle_soyad.text(),
                'dogum_tarihi': self.ogr_ekle_dogumTarhi.text(),
                'telefon': self.ogr_ekle_telefon.text(),
                'mail_adresi': self.ogr_ekle_mail.text(),
                'ev_adresi': self.ogr_ekle_evAdresi.text(),
                'cinsiyet': self.ogr_ekle_cinsiyet.currentText(),
                'ogrenci_no': self.ogr_ekle_okulNumarasi.text()
            }
            # is there any empyt field
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in learnerData.values()].count('') > 0 else False) is not False: return
            # is name and surname fields alphabetical?
            if (False if learnerData['ad'].isalpha() and learnerData['soyad'].isalpha() else warning("Lütfen Ad ve Soyad Alanında Sadece Harf Kullanınız").exec_()) is not False: return
            # is day of birth in the correct format?
            if (warning("Lütfen Belirtilen Formatta Geçerli Bir Doğum Tarihi Giriniz").exec_() if learnerData['dogum_tarihi'].count('.') > 2 or learnerData['dogum_tarihi'].count('.') < 2 else False) is not False: return
            # is phone number 11 digits? or startswith '0'? or numeric?
            if (False if learnerData['telefon'].startswith('0') and len(learnerData['telefon'].replace(' ', '')) == 11 and learnerData['telefon'].isnumeric() else warning("Lütfen Doğru Formatta Geçerli Bir Telefon Numarası Giriniz").exec_()) is not False: return
            # is school number numeric?
            if (False if learnerData['ogrenci_no'].isnumeric() else warning("Okul Numarası Sedece Rakamlardan Oluşmalıdır.").exec_()) is not False: return
            # same learner number control
            if (warning("Girilen Öğrenci Numarasını Başka Bir Öğrenci Kullanıyor.").exec_() if self.sql.sameNumberLearnerControl(learnerData['ogrenci_no']) else False) is not False:return
            # adding new learner
            self.sql.addLearner(learnerData)
            # clear the QLineEdit Fields
            [i.clear() for i in [self.ogr_ekle_ad, self.ogr_ekle_soyad, self.ogr_ekle_dogumTarhi, self.ogr_ekle_telefon,
                                 self.ogr_ekle_mail, self.ogr_ekle_evAdresi,
                                 self.ogr_ekle_okulNumarasi]]
            warning('Öğrenci Ekleme İşlemi Başarılı').exec_()
            # for update widgets
            self.setInfo()
        def bilgileriGetir():
            if self.combo_edit_learners.currentText()!= "":
                theLearnerNumber = self.combo_edit_learners.currentText().split(" ")[-1]
                thelearnerInfo=(self.sql.getTheLearnerInfo(theLearnerNumber))[0]
                lineEdits=[self.ogr_edit_ad,self.ogr_edit_soyad,self.ogr_edit_dogumTarihi,self.ogr_edit_telefon,self.ogr_edit_mail,self.ogr_edit_evAdresi]
                Info=[thelearnerInfo['ad'],thelearnerInfo['soyad'],thelearnerInfo['dogum_tarihi'],thelearnerInfo['telefon'],thelearnerInfo['mail_adresi'],thelearnerInfo['ev_adresi']]
                [a.setText(str(b)) for a,b in zip(lineEdits,Info)]
                self.ogr_edit_cinsiyet.setCurrentIndex(0) if (thelearnerInfo['cinsiyet'] == 'Erkek') else self.ogr_edit_cinsiyet.setCurrentIndex(1)
                [i.show() for i in self.ogr_duzenle_show_hide]
            if self.combo_yerlestir_learners.currentText()!="":
                self.label_yerlestir_learners.setText(self.combo_yerlestir_learners.currentText())
                self.label_yerlestir_learners.show()
            if self.combo_yerlestir_classes.currentText()!="":
                self.label_yerlestir_class.setText(self.combo_yerlestir_classes.currentText())
                self.label_yerlestir_class.show()


        def ogrenciGuncelle():
            learnerData = {
                'ad': self.ogr_edit_ad.text(),
                'soyad': self.ogr_edit_soyad.text(),
                'dogum_tarihi': self.ogr_edit_dogumTarihi.text(),
                'telefon': self.ogr_edit_telefon.text(),
                'mail_adresi': self.ogr_edit_mail.text(),
                'ev_adresi': self.ogr_edit_evAdresi.text(),
                'cinsiyet': self.ogr_edit_cinsiyet.currentText()
            }
            # is there any empyt field
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in learnerData.values()].count(
                    '') > 0 else False) is not False: return

            # is name and surname fields alphabetical?
            if (False if learnerData['ad'].isalpha() and learnerData['soyad'].isalpha() else warning(
                    "Lütfen Ad ve Soyad Alanında Sadece Harf Kullanınız").exec_()) is not False: return

            # is day of birth in the correct format?
            if (warning("Lütfen Belirtilen Formatta Geçerli Bir Doğum Tarihi Giriniz").exec_() if learnerData[
                                                                                                      'dogum_tarihi'].count(
                '.') > 2 or learnerData['dogum_tarihi'].count('.') < 2 else False) is not False: return

            # is phone number 11 digits? or startswith '0'? or numeric?
            if (False if learnerData['telefon'].startswith('0') and len(
                    learnerData['telefon'].replace(' ', '')) == 11 and learnerData['telefon'].isnumeric() else warning(
                "Lütfen Doğru Formatta Geçerli Bir Telefon Numarası Giriniz").exec_()) is not False: return

            #adding current studens number to learnerData
            learnerData['ogrenci_no']=self.combo_edit_learners.currentText().split(" ")[-1]

            #update
            self.sql.updateLearnerInfo(learnerData)

            #Hide the QLineEdits fields
            [i.hide() for i in self.ogr_duzenle_show_hide]
            warning('Öğrenci Güncelleme İşlemi Başarılı').exec_()

            # for update widgets
        def ogrenciSil():
            theLearnerNumber=self.combo_edit_learners.currentText().split(" ")[-1]
            # delete
            self.sql.theLearnerDelete(theLearnerNumber)
            # Hide the QLineEdits fields
            [i.hide() for i in self.ogr_duzenle_show_hide]
            warning('Öğrenci Silme İşlemi Başarılı').exec_()
            # for update widgets
            self.setInfo()
        def ogrenciYerlestir():
            if self.label_yerlestir_class.isHidden() or self.label_yerlestir_learners.isHidden():
                warning('Lütfen Sınıf Ve Öğrenci Seçimi Yapınız').exec_()
            else:
                self.sql.setLearnerToEmplace([self.combo_yerlestir_classes.currentText().split(" ")[0],self.combo_yerlestir_learners.currentText().split(" ")[-1]])
                self.setInfo()
                self.label_yerlestir_learners.hide()
                self.label_yerlestir_class.hide()
                warning('Öğrenci - Sınıf Yerleştirme İşlemi Başarılı').exec_()


        sender=self.sender()
        if str(sender.objectName())=="combo_edit_learners":
            bilgileriGetir()
        elif str(sender.objectName())=="combo_yerlestir_classes":
            bilgileriGetir()
        elif str(sender.objectName())=="combo_yerlestir_learners":
            bilgileriGetir()
        elif sender.text()=="Öğrenci Ekle":
            ogrenciEkle()
        elif sender.text()=="BİLGİLERİ GETİR":
            bilgileriGetir()
        elif sender.text()=="Öğrenci Düzenle":
            warning('Lütfen öncelikle herhangi bir öğrenci bilgisi getirin').exec_() if self.ogr_edit_ad.isHidden() else ogrenciGuncelle()
        elif sender.text()=="Öğrenci Sil":
            warning('Lütfen öncelikle herhangi bir öğrenci bilgisi getirin').exec_() if self.ogr_edit_ad.isHidden() else ogrenciSil()
        elif sender.text()=="Yerleştir":
            ogrenciYerlestir()
        elif sender.text()=="Ders Kaydet":
            pass

    def dersSinifSection(self):
        def addLesson():
            lessonData = {
                'ders_kod': self.ders_ekle_kod.text(),
                'ders_ismi': self.ders_ekle_isim.text(),
                'ders_tanim': self.ders_ekle_tanim.toPlainText(),
                'ders_kredi': self.ders_ekle_kredi.text(),
                'ders_akts': self.ders_ekle_akts.text(),
                'vize_yuzde': self.ders_ekle_vizeYuzde.text(),
                'final_yuzde': self.ders_ekle_finalYuzde.text()
            }
            # is there any empyt field
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in lessonData.values()].count('') > 0 else False) is not False: return
            # is lesson code is numeric?
            if (False if lessonData['ders_kod'].isnumeric() else warning("Lütfen Doğru Formatta Geçerli Bir Telefon Numarası Giriniz").exec_()) is not False: return
            # is lesson akts is numeric?
            if (False if lessonData['ders_akts'].isnumeric() else warning("Lütfen Doğru Formatta Geçerli Bir Telefon Numarası Giriniz").exec_()) is not False: return
            # is lesson credit is numeric?
            if (False if lessonData['ders_kredi'].isnumeric() else warning("Lütfen Doğru Formatta Geçerli Bir Telefon Numarası Giriniz").exec_()) is not False: return
            #is exam percentace correct number?
            if (False if lessonData['vize_yuzde'].isnumeric() and int(lessonData['vize_yuzde'])<101 and int(lessonData['vize_yuzde']) >0 else warning("Lütfen Vize Yüzdesi İçin 0-101 Arasında Bir Sayı Giriniz").exec_()) is not False: return
            if (False if lessonData['final_yuzde'].isnumeric() and int(lessonData['final_yuzde'])<101 and int(lessonData['final_yuzde']) >0 else warning("Lütfen Vize Yüzdesi İçin 0-101 Arasında Bir Sayı Giriniz").exec_()) is not False: return
            # adding new learner
            self.sql.addLesson(lessonData)
            # clear the QLineEdit Fields
            [i.clear() for i in [self.ders_ekle_kod, self.ders_ekle_isim, self.ders_ekle_tanim, self.ders_ekle_kredi,self.ders_ekle_akts, self.ders_ekle_vizeYuzde, self.ders_ekle_finalYuzde,]]
            warning('Ders Ekleme İşlemi Başarılı').exec_()
            # for update widgets
            self.setInfo()
        def addClass():
            classData = {
                'sinif_id': self.sinif_ekle_kod.text(),
                'sinif_ismi': self.sinif_ekle_isim.text(),
            }
            # is there any empyt field
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in classData.values()].count('') > 0 else False) is not False: return
            # is class code is numeric?
            if (False if classData['sinif_id'].isnumeric() else warning("Lütfen Sadece Rakamlardan Oluşan Bir Ders Kodu Giriniz").exec_()) is not False: return
            # same learner number control
            if (warning("Girilen Sınıf Kodu Kullanımda.").exec_() if self.sql.sameClassCodeControl(classData['sinif_id']) else False) is not False: return
            # adding new class
            self.sql.addClass(classData)
            # clear the QLineEdit Fields
            [i.clear() for i in [self.sinif_ekle_isim,self.sinif_ekle_kod]]
            warning('Sınıf Ekleme İşlemi Başarılı').exec_()
            # for update widgets
            self.setInfo()


        sender=self.sender()
        if sender.text()=="Ders Ekle":
            addLesson()
        elif sender.text()=="Sınıf Ekle":
            addClass()

    def showWidget(self):
        # IS MENU OPEN OR CLOSE? | IS MENU OR SUB MENU | SET CSS
        def is_Open(is_first_menu,whichmenu):

            # adding last opened or closed menu for setting style css
            self.last_menu.append(whichmenu[0])

            #not necessary more than 3
            if len(self.last_menu) > 3:
                self.last_menu.remove(self.last_menu[0])

            #is menu open or not?
            if self.open_close_control=="close":
                self.open_close_control="open"

                #is it menu or submenu
                if is_first_menu:
                    self.mainStack.setStyleSheet("QWidget{background:rgba(0,0,0,0.1)}")
                    return True
                else:
                    self.menuStack.hide()
                    self.mainStack.setStyleSheet("QWidget{background:rgba(0,0,0,0.0001)}")

            elif self.open_close_control=="open":
                if is_first_menu:
                    if self.last_menu[-1]==self.last_menu[-2]:
                        #running when clicked same menu
                        self.open_close_control = "close"
                        self.mainStack.setStyleSheet("QWidget{background:rgba(0,0,0,0.0001)}")
                        #to show last opened QWidget
                        setCss([self.opened_menu[-1]])
                        return False
                    else:
                        self.open_close_control="open"
                        self.menuStack.hide()
                        self.mainStack.setStyleSheet("QWidget{background:rgba(0,0,0,0.1)}")
                        return True
                else:
                    #this block is running when clicked any submenu and adding to opened_menu_list
                    self.opened_menu.append(whichmenu[1])
                    self.mainStack.setStyleSheet("QWidget{background:rgba(0,0,0,0.0001)}")
                    self.menuStack.hide()
                    self.hesapWidget.hide()
        def setCss(tabs):
            current_menu_css = "QPushButton{background:rgba(45,54,76,0.93);border:none;border-bottom:1px solid rgb(38,46,65);color:silver;font-size:28px;}QPushButton:hover{background:rgba(40,49,71,0.97);border:none;color:silver;border-bottom:1px solid rgb(38,46,65)}"
            current_submenu_css = "QPushButton{background:rgba(45,54,76,0.99);border:none;color:silver;font-size:18px;border-bottom:1px solid rgb(38,46,65)}QPushButton:hover{background:rgba(35,43,62,0.99);border:none;color:white;border-bottom:1px solid rgb(38,46,65)}"
            new_menu_css = "QPushButton{background:rgba(101,52,172,0.93);border:none;color:white;font-size:28px;border-top:none}"

            new_submenu_css="QPushButton{background:rgba(101,52,172,0.93);border:none;color:silver;font-size:18px;}QPushButton:hover{background:rgba(91,47,155,0.97);border:none;color:white;}"
            menuList=[self.btn_profil,self.btn_ders,self.btn_ogrenci,self.btn_yoklama_not,self.btn_hesap]
            subMenuList=[self.btn_ogrenci_duzenle,self.btn_ogrenci_ekle,self.btn_ogrenci_goruntule,self.btn_ders_ekle,self.btn_ders_duzenle,self.btn_ders_goruntule,self.btn_not_gir,self.btn_yoklama_al,self.btn_hesap_setting]

            # tabs --> argument is list (first index = menu , submenu = all list without first index)

            #for a different menu added later
            clicked_account_css="QPushButton{background:rgba(0, 0, 0,0.08);border-radius:none;color:white;border-bottom:3px solid rgba(101,52,172,0.93);font-size:28px;}"
            if tabs[0]==self.btn_hesap:
                tabs[0].setStyleSheet(clicked_account_css)
                menuList.remove(tabs[0])
                [menu.setStyleSheet(current_menu_css) for menu in menuList]
                return

            #set style to the new menu
            tabs[0].setStyleSheet(new_menu_css)
            #remove menu from all lists
            menuList.remove(tabs[0])
            tabs.remove(tabs[0])
            #set style to the new submenu
            [theSubTabs.setStyleSheet(new_submenu_css) for theSubTabs in tabs]
            #remove submenu from submenu list
            [subMenuList.remove(removedSubtab) for removedSubtab in tabs]
            #set style to the other menu
            [menu.setStyleSheet(current_menu_css) for menu in menuList]
            #set style to the other submenu
            [subMenu.setStyleSheet(current_submenu_css) for subMenu in subMenuList]

        sender=self.sender()

        if sender.text()=="PROFİL":
            self.hesapWidget.hide()
            self.menuStack.hide()
            self.mainStack.setCurrentWidget(self.qw_profil)
            self.mainStack.setStyleSheet("QWidget{background:rgba(0,0,0,0.001)}")
            is_Open(False,["profil",self.btn_profil])
            setCss([self.btn_profil])

        elif sender.text()=="DERS\nSINIF":
            if is_Open(True,["ders",self.btn_ders]):
                self.hesapWidget.hide()
                self.menuStack.setCurrentWidget(self.menu_ders)
                self.menuStack.show()
                setCss([self.btn_ders,self.btn_ders_ekle,self.btn_ders_duzenle,self.btn_ders_goruntule])
            else:
                self.menuStack.hide()

        elif sender.text()=="ÖĞRENCİ":
            if is_Open(True,["ogrenci",self.btn_ogrenci]):
                self.hesapWidget.hide()
                self.menuStack.setCurrentWidget(self.menu_ogrenci)
                self.menuStack.show()
                setCss([self.btn_ogrenci,self.btn_ogrenci_ekle,self.btn_ogrenci_duzenle,self.btn_ogrenci_goruntule])
            else:
                self.menuStack.hide()

        elif sender.text()=="\nYOKLAMA\nNOT":
            if is_Open(True,["yoklama",self.btn_yoklama_not]):
                self.hesapWidget.hide()
                self.menuStack.setCurrentWidget(self.menu_yoklama_not)
                self.menuStack.show()
                setCss([self.btn_yoklama_not,self.btn_yoklama_al,self.btn_not_gir])
            else:
                self.menuStack.hide()

        elif sender.text()=="HESAP":
            if is_Open(True, ["hesap", self.btn_hesap]):
                self.hesapWidget.show()
                setCss([self.btn_hesap,self.btn_hesap_setting])
            else:
                self.hesapWidget.hide()
        elif sender.text()=="Hesap Ayarları":
            self.mainStack.setCurrentWidget(self.qw_hesap)

            is_Open(False,['hesap_ayarlari',self.btn_hesap])
        elif sender.text()=="Ö. EKLE":
            self.ogrenciStack.setCurrentWidget(self.qw_ogrenci_ekle)
            self.mainStack.setCurrentWidget(self.qw_ogrenci)
            is_Open(False,["o_ekle",self.btn_ogrenci])
        elif sender.text()=="Ö. DÜZENLE":
            self.ogrenciStack.setCurrentWidget(self.qw_ogrenci_duzenle)
            self.mainStack.setCurrentWidget(self.qw_ogrenci)
            is_Open(False,["o_duzenle",self.btn_ogrenci])
            #choose you a learner?
            [i.hide() for i in self.ogr_duzenle_show_hide]
            is_Open(False, ["o_duzenle", self.btn_ogrenci])



        elif sender.text()=="ÖĞRENCİ \nDERS-SINIF KAYDI":
            self.ogrenciStack.setCurrentWidget(self.qw_ogrenci_goruntule)
            self.mainStack.setCurrentWidget(self.qw_ogrenci)
            is_Open(False,["o_goruntule",self.btn_ogrenci])
        elif sender.text()=="DERS - SINIF\nEKLE":
            self.dersStack.setCurrentWidget(self.qw_ders_ekle)
            self.mainStack.setCurrentWidget(self.qw_ders)
            is_Open(False,["d_ekle",self.btn_ders])
        elif sender.text()=="DERS - SINIF\nDÜZENLE":
            self.dersStack.setCurrentWidget(self.qw_ders_duzenle)
            self.mainStack.setCurrentWidget(self.qw_ders)
            is_Open(False,["d_duzenle",self.btn_ders])


        elif sender.text()=="DERS - SINIF\nGÖRÜNTÜLE":
            self.dersStack.setCurrentWidget(self.qw_ders_goruntule)
            self.mainStack.setCurrentWidget(self.qw_ders)
            is_Open(False,["d_goruntule",self.btn_ders])


        elif sender.text()=="YOKLAMA AL":
            self.yoklamaNotStack.setCurrentWidget(self.qw_yoklama_al)
            self.mainStack.setCurrentWidget(self.qw_yoklama)
            is_Open(False,["yoklama_al",self.btn_yoklama_not])
        elif sender.text()=="NOT GİR":
            self.yoklamaNotStack.setCurrentWidget(self.qw_not_gir)
            self.mainStack.setCurrentWidget(self.qw_yoklama)
            is_Open(False,["not",self.btn_yoklama_not])






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
app=QApplication(sys.argv)
w=ogrenciTakip()
w.show()
sys.exit(app.exec_())


