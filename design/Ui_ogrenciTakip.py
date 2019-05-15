# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lenovo\Desktop\PYTHON OTOMOSYON\design\ogrenciTakip.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 780)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 780))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/yu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1250, 780))
        self.centralwidget.setMaximumSize(QtCore.QSize(1250, 780))
        self.centralwidget.setStyleSheet("background:url(:images/images/main_background.jpg);\n"
"\n"
"QPushButton{\n"
"color:green;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1250, 780))
        self.frame.setMinimumSize(QtCore.QSize(1250, 780))
        self.frame.setMaximumSize(QtCore.QSize(1250, 780))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame{\n"
"background:rgba(53, 63, 89,0.9);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_profil = QtWidgets.QPushButton(self.frame)
        self.btn_profil.setGeometry(QtCore.QRect(0, 100, 175, 170))
        self.btn_profil.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_profil.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_profil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_profil.setStyleSheet("QPushButton{\n"
"background:rgba(101,52,172,0.93);border:none;color:white;font-size:28px;\n"
"}\n"
"")
        self.btn_profil.setObjectName("btn_profil")
        self.gorevCubugu = QtWidgets.QFrame(self.frame)
        self.gorevCubugu.setGeometry(QtCore.QRect(0, 40, 1250, 60))
        self.gorevCubugu.setStyleSheet("QFrame{\n"
"background-color:rgba(25,35,49,0.699);\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.gorevCubugu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gorevCubugu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gorevCubugu.setObjectName("gorevCubugu")
        self.label_department_name = QtWidgets.QLabel(self.gorevCubugu)
        self.label_department_name.setGeometry(QtCore.QRect(12, 32, 391, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_department_name.setFont(font)
        self.label_department_name.setStyleSheet("color:silver;\n"
"background:transparent;\n"
"border:none;")
        self.label_department_name.setObjectName("label_department_name")
        self.btn_hesap = QtWidgets.QPushButton(self.gorevCubugu)
        self.btn_hesap.setGeometry(QtCore.QRect(1095, 0, 155, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_hesap.setFont(font)
        self.btn_hesap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_hesap.setStyleSheet("\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(0, 0, 0,0.08);\n"
"color:white;\n"
"border-bottom:3px solid rgba(101,52,172,0.93);\n"
"}\n"
"QPushButton{background:rgba(45,54,76,0.93);border:none;border-bottom:1px solid rgb(38,46,65);color:silver;font-size:28px;}\n"
"")
        self.btn_hesap.setObjectName("btn_hesap")
        self.label_username = QtWidgets.QLabel(self.gorevCubugu)
        self.label_username.setGeometry(QtCore.QRect(12, 3, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color:silver;\n"
"background:transparent;\n"
"border:none;")
        self.label_username.setObjectName("label_username")
        self.btn_ogrenci = QtWidgets.QPushButton(self.frame)
        self.btn_ogrenci.setGeometry(QtCore.QRect(0, 270, 175, 170))
        self.btn_ogrenci.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ogrenci.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ogrenci.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenci.setStyleSheet("\n"
"QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:28px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(40,49,71,0.97);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}")
        self.btn_ogrenci.setObjectName("btn_ogrenci")
        self.btn_ders = QtWidgets.QPushButton(self.frame)
        self.btn_ders.setGeometry(QtCore.QRect(0, 440, 175, 170))
        self.btn_ders.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ders.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ders.setStyleSheet("\n"
"QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:28px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(40,49,71,0.97);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}")
        self.btn_ders.setObjectName("btn_ders")
        self.btn_yoklama_not = QtWidgets.QPushButton(self.frame)
        self.btn_yoklama_not.setGeometry(QtCore.QRect(0, 610, 175, 170))
        self.btn_yoklama_not.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_yoklama_not.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_yoklama_not.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_yoklama_not.setStyleSheet("\n"
"QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:28px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(40,49,71,0.97);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}")
        self.btn_yoklama_not.setObjectName("btn_yoklama_not")
        self.mainStack = QtWidgets.QStackedWidget(self.frame)
        self.mainStack.setGeometry(QtCore.QRect(175, 100, 1075, 700))
        self.mainStack.setStyleSheet("QWidget{\n"
"background:rgba(0,0,0,0.0001)\n"
"}")
        self.mainStack.setObjectName("mainStack")
        self.qw_profil = QtWidgets.QWidget()
        self.qw_profil.setStyleSheet("")
        self.qw_profil.setObjectName("qw_profil")
        self.mainStack.addWidget(self.qw_profil)
        self.qw_ders = QtWidgets.QWidget()
        self.qw_ders.setObjectName("qw_ders")
        self.dersStack = QtWidgets.QStackedWidget(self.qw_ders)
        self.dersStack.setGeometry(QtCore.QRect(0, 0, 1075, 700))
        self.dersStack.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.97);\n"
"border:none;\n"
"color:white;\n"
"}\n"
"")
        self.dersStack.setObjectName("dersStack")
        self.qw_ders_ekle = QtWidgets.QWidget()
        self.qw_ders_ekle.setStyleSheet("")
        self.qw_ders_ekle.setObjectName("qw_ders_ekle")
        self.label_18 = QtWidgets.QLabel(self.qw_ders_ekle)
        self.label_18.setGeometry(QtCore.QRect(20, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.qw_ders_ekle)
        self.label_19.setGeometry(QtCore.QRect(93, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.label_24 = QtWidgets.QLabel(self.qw_ders_ekle)
        self.label_24.setGeometry(QtCore.QRect(128, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_24.setObjectName("label_24")
        self.frame_5 = QtWidgets.QFrame(self.qw_ders_ekle)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1091, 691))
        self.frame_5.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.2);\n"
"}\n"
"QLineEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"}\n"
"QTextEdit{\n"
"font-size:24px;;\n"
"color:white;\n"
"border:none;\n"
"border-radius:7px;\n"
"background:rgba(0,0,0,0.11);\n"
"}\n"
"QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:silver;\n"
"background:transparent\n"
"}\n"
"QCheckBox:hover{\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.ders_ekle_kod = QtWidgets.QLineEdit(self.frame_5)
        self.ders_ekle_kod.setGeometry(QtCore.QRect(47, 409, 448, 41))
        self.ders_ekle_kod.setText("")
        self.ders_ekle_kod.setMaxLength(24)
        self.ders_ekle_kod.setObjectName("ders_ekle_kod")
        self.ders_ekle_isim = QtWidgets.QLineEdit(self.frame_5)
        self.ders_ekle_isim.setGeometry(QtCore.QRect(47, 349, 448, 41))
        self.ders_ekle_isim.setText("")
        self.ders_ekle_isim.setMaxLength(24)
        self.ders_ekle_isim.setFrame(True)
        self.ders_ekle_isim.setObjectName("ders_ekle_isim")
        self.btn_dersEkle = QtWidgets.QPushButton(self.frame_5)
        self.btn_dersEkle.setGeometry(QtCore.QRect(47, 598, 447, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_dersEkle.setFont(font)
        self.btn_dersEkle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dersEkle.setObjectName("btn_dersEkle")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(51, 70, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:36px;")
        self.label_11.setObjectName("label_11")
        self.label_33 = QtWidgets.QLabel(self.frame_5)
        self.label_33.setGeometry(QtCore.QRect(56, 124, 411, 41))
        self.label_33.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_33.setObjectName("label_33")
        self.ders_ekle_tanim = QtWidgets.QTextEdit(self.frame_5)
        self.ders_ekle_tanim.setGeometry(QtCore.QRect(47, 198, 450, 131))
        self.ders_ekle_tanim.setObjectName("ders_ekle_tanim")
        self.ders_ekle_akts = QtWidgets.QLineEdit(self.frame_5)
        self.ders_ekle_akts.setGeometry(QtCore.QRect(47, 469, 209, 41))
        self.ders_ekle_akts.setText("")
        self.ders_ekle_akts.setMaxLength(24)
        self.ders_ekle_akts.setObjectName("ders_ekle_akts")
        self.ders_ekle_kredi = QtWidgets.QLineEdit(self.frame_5)
        self.ders_ekle_kredi.setGeometry(QtCore.QRect(286, 469, 209, 41))
        self.ders_ekle_kredi.setText("")
        self.ders_ekle_kredi.setMaxLength(24)
        self.ders_ekle_kredi.setObjectName("ders_ekle_kredi")
        self.ders_ekle_finalYuzde = QtWidgets.QLineEdit(self.frame_5)
        self.ders_ekle_finalYuzde.setGeometry(QtCore.QRect(286, 529, 209, 41))
        self.ders_ekle_finalYuzde.setText("")
        self.ders_ekle_finalYuzde.setMaxLength(24)
        self.ders_ekle_finalYuzde.setObjectName("ders_ekle_finalYuzde")
        self.ders_ekle_vizeYuzde = QtWidgets.QLineEdit(self.frame_5)
        self.ders_ekle_vizeYuzde.setGeometry(QtCore.QRect(47, 529, 209, 41))
        self.ders_ekle_vizeYuzde.setText("")
        self.ders_ekle_vizeYuzde.setMaxLength(24)
        self.ders_ekle_vizeYuzde.setObjectName("ders_ekle_vizeYuzde")
        self.label_34 = QtWidgets.QLabel(self.frame_5)
        self.label_34.setGeometry(QtCore.QRect(586, 124, 441, 41))
        self.label_34.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_5)
        self.label_35.setGeometry(QtCore.QRect(581, 70, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:36px;")
        self.label_35.setObjectName("label_35")
        self.sinif_ekle_kod = QtWidgets.QLineEdit(self.frame_5)
        self.sinif_ekle_kod.setGeometry(QtCore.QRect(577, 250, 448, 41))
        self.sinif_ekle_kod.setText("")
        self.sinif_ekle_kod.setMaxLength(11)
        self.sinif_ekle_kod.setObjectName("sinif_ekle_kod")
        self.sinif_ekle_isim = QtWidgets.QLineEdit(self.frame_5)
        self.sinif_ekle_isim.setGeometry(QtCore.QRect(577, 190, 448, 41))
        self.sinif_ekle_isim.setText("")
        self.sinif_ekle_isim.setMaxLength(65)
        self.sinif_ekle_isim.setFrame(True)
        self.sinif_ekle_isim.setObjectName("sinif_ekle_isim")
        self.btn_sinifEkle = QtWidgets.QPushButton(self.frame_5)
        self.btn_sinifEkle.setGeometry(QtCore.QRect(578, 319, 447, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_sinifEkle.setFont(font)
        self.btn_sinifEkle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sinifEkle.setObjectName("btn_sinifEkle")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(580, 400, 441, 241))
        self.frame_6.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.6);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_40 = QtWidgets.QLabel(self.frame_6)
        self.label_40.setGeometry(QtCore.QRect(30, 80, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(35)
        font.setUnderline(False)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color:white;\n"
"background:transparent;")
        self.label_40.setObjectName("label_40")
        self.ders_ekle_kod.raise_()
        self.ders_ekle_isim.raise_()
        self.btn_dersEkle.raise_()
        self.label_11.raise_()
        self.label_33.raise_()
        self.ders_ekle_tanim.raise_()
        self.ders_ekle_akts.raise_()
        self.ders_ekle_kredi.raise_()
        self.ders_ekle_finalYuzde.raise_()
        self.ders_ekle_vizeYuzde.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.sinif_ekle_kod.raise_()
        self.sinif_ekle_isim.raise_()
        self.btn_sinifEkle.raise_()
        self.frame_6.raise_()
        self.dersStack.addWidget(self.qw_ders_ekle)
        self.qw_ders_duzenle = QtWidgets.QWidget()
        self.qw_ders_duzenle.setObjectName("qw_ders_duzenle")
        self.label_20 = QtWidgets.QLabel(self.qw_ders_duzenle)
        self.label_20.setGeometry(QtCore.QRect(53, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.qw_ders_duzenle)
        self.label_21.setGeometry(QtCore.QRect(20, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_21.setObjectName("label_21")
        self.label_25 = QtWidgets.QLabel(self.qw_ders_duzenle)
        self.label_25.setGeometry(QtCore.QRect(88, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_25.setObjectName("label_25")
        self.dersStack.addWidget(self.qw_ders_duzenle)
        self.qw_ders_goruntule = QtWidgets.QWidget()
        self.qw_ders_goruntule.setObjectName("qw_ders_goruntule")
        self.label_22 = QtWidgets.QLabel(self.qw_ders_goruntule)
        self.label_22.setGeometry(QtCore.QRect(53, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.qw_ders_goruntule)
        self.label_23.setGeometry(QtCore.QRect(20, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_23.setObjectName("label_23")
        self.label_26 = QtWidgets.QLabel(self.qw_ders_goruntule)
        self.label_26.setGeometry(QtCore.QRect(88, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_26.setObjectName("label_26")
        self.dersStack.addWidget(self.qw_ders_goruntule)
        self.mainStack.addWidget(self.qw_ders)
        self.qw_ogrenci = QtWidgets.QWidget()
        self.qw_ogrenci.setObjectName("qw_ogrenci")
        self.ogrenciStack = QtWidgets.QStackedWidget(self.qw_ogrenci)
        self.ogrenciStack.setGeometry(QtCore.QRect(0, 0, 1075, 700))
        self.ogrenciStack.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.97);\n"
"border:none;\n"
"color:white;\n"
"}")
        self.ogrenciStack.setObjectName("ogrenciStack")
        self.qw_ogrenci_ekle = QtWidgets.QWidget()
        self.qw_ogrenci_ekle.setObjectName("qw_ogrenci_ekle")
        self.label_4 = QtWidgets.QLabel(self.qw_ogrenci_ekle)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.qw_ogrenci_ekle)
        self.label_10.setGeometry(QtCore.QRect(73, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_15 = QtWidgets.QLabel(self.qw_ogrenci_ekle)
        self.label_15.setGeometry(QtCore.QRect(107, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.frame_3 = QtWidgets.QFrame(self.qw_ogrenci_ekle)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1091, 691))
        self.frame_3.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.2);\n"
"}\n"
"QLineEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}\n"
"QLineEdit:hover{\n"
"background:rgba(0,0,0,0.04);\n"
"}\n"
"QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(68, 117, 222)\n"
"}\n"
"QCheckBox{\n"
"color:silver;\n"
"background:transparent\n"
"}\n"
"QCheckBox:hover{\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.ogr_ekle_ad = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_ad.setGeometry(QtCore.QRect(46, 251, 461, 61))
        self.ogr_ekle_ad.setText("")
        self.ogr_ekle_ad.setMaxLength(24)
        self.ogr_ekle_ad.setObjectName("ogr_ekle_ad")
        self.ogr_ekle_soyad = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_soyad.setGeometry(QtCore.QRect(563, 251, 461, 61))
        self.ogr_ekle_soyad.setText("")
        self.ogr_ekle_soyad.setMaxLength(24)
        self.ogr_ekle_soyad.setFrame(True)
        self.ogr_ekle_soyad.setObjectName("ogr_ekle_soyad")
        self.ogr_ekle_dogumTarhi = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_dogumTarhi.setGeometry(QtCore.QRect(46, 331, 461, 61))
        self.ogr_ekle_dogumTarhi.setText("")
        self.ogr_ekle_dogumTarhi.setMaxLength(24)
        self.ogr_ekle_dogumTarhi.setObjectName("ogr_ekle_dogumTarhi")
        self.ogr_ekle_mail = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_mail.setGeometry(QtCore.QRect(46, 411, 461, 61))
        self.ogr_ekle_mail.setText("")
        self.ogr_ekle_mail.setMaxLength(40)
        self.ogr_ekle_mail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_ekle_mail.setObjectName("ogr_ekle_mail")
        self.ogr_ekle_evAdresi = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_evAdresi.setGeometry(QtCore.QRect(563, 411, 461, 61))
        self.ogr_ekle_evAdresi.setText("")
        self.ogr_ekle_evAdresi.setMaxLength(40)
        self.ogr_ekle_evAdresi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_ekle_evAdresi.setObjectName("ogr_ekle_evAdresi")
        self.btn_ogrenciEkle = QtWidgets.QPushButton(self.frame_3)
        self.btn_ogrenciEkle.setGeometry(QtCore.QRect(560, 590, 470, 64))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_ogrenciEkle.setFont(font)
        self.btn_ogrenciEkle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciEkle.setObjectName("btn_ogrenciEkle")
        self.ogr_ekle_telefon = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_telefon.setGeometry(QtCore.QRect(563, 331, 461, 61))
        self.ogr_ekle_telefon.setText("")
        self.ogr_ekle_telefon.setMaxLength(40)
        self.ogr_ekle_telefon.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_ekle_telefon.setObjectName("ogr_ekle_telefon")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(51, 70, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:36px;")
        self.label.setObjectName("label")
        self.ogr_ekle_cinsiyet = QtWidgets.QComboBox(self.frame_3)
        self.ogr_ekle_cinsiyet.setGeometry(QtCore.QRect(563, 491, 461, 61))
        self.ogr_ekle_cinsiyet.setStyleSheet("font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.ogr_ekle_cinsiyet.setObjectName("ogr_ekle_cinsiyet")
        self.ogr_ekle_cinsiyet.addItem("")
        self.ogr_ekle_cinsiyet.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(56, 124, 571, 41))
        self.label_5.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_5.setObjectName("label_5")
        self.ogr_ekle_okulNumarasi = QtWidgets.QLineEdit(self.frame_3)
        self.ogr_ekle_okulNumarasi.setGeometry(QtCore.QRect(46, 491, 461, 61))
        self.ogr_ekle_okulNumarasi.setText("")
        self.ogr_ekle_okulNumarasi.setMaxLength(40)
        self.ogr_ekle_okulNumarasi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_ekle_okulNumarasi.setObjectName("ogr_ekle_okulNumarasi")
        self.label_15.raise_()
        self.label_4.raise_()
        self.label_10.raise_()
        self.frame_3.raise_()
        self.ogrenciStack.addWidget(self.qw_ogrenci_ekle)
        self.qw_ogrenci_duzenle = QtWidgets.QWidget()
        self.qw_ogrenci_duzenle.setObjectName("qw_ogrenci_duzenle")
        self.label_13 = QtWidgets.QLabel(self.qw_ogrenci_duzenle)
        self.label_13.setGeometry(QtCore.QRect(73, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(self.qw_ogrenci_duzenle)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_16 = QtWidgets.QLabel(self.qw_ogrenci_duzenle)
        self.label_16.setGeometry(QtCore.QRect(107, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.frame_4 = QtWidgets.QFrame(self.qw_ogrenci_duzenle)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1075, 700))
        self.frame_4.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.2);\n"
"}\n"
"QLineEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}\n"
"QLineEdit:hover{\n"
"background:rgba(0,0,0,0.04);\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:silver;\n"
"background:transparent\n"
"}\n"
"QCheckBox:hover{\n"
"color:white;\n"
"}\n"
"QTextEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.ogr_edit_ad = QtWidgets.QLineEdit(self.frame_4)
        self.ogr_edit_ad.setEnabled(True)
        self.ogr_edit_ad.setGeometry(QtCore.QRect(46, 310, 461, 61))
        self.ogr_edit_ad.setText("")
        self.ogr_edit_ad.setMaxLength(24)
        self.ogr_edit_ad.setObjectName("ogr_edit_ad")
        self.ogr_edit_soyad = QtWidgets.QLineEdit(self.frame_4)
        self.ogr_edit_soyad.setGeometry(QtCore.QRect(563, 310, 461, 61))
        self.ogr_edit_soyad.setText("")
        self.ogr_edit_soyad.setMaxLength(24)
        self.ogr_edit_soyad.setFrame(True)
        self.ogr_edit_soyad.setObjectName("ogr_edit_soyad")
        self.ogr_edit_dogumTarihi = QtWidgets.QLineEdit(self.frame_4)
        self.ogr_edit_dogumTarihi.setGeometry(QtCore.QRect(46, 390, 461, 61))
        self.ogr_edit_dogumTarihi.setText("")
        self.ogr_edit_dogumTarihi.setMaxLength(24)
        self.ogr_edit_dogumTarihi.setObjectName("ogr_edit_dogumTarihi")
        self.ogr_edit_mail = QtWidgets.QLineEdit(self.frame_4)
        self.ogr_edit_mail.setGeometry(QtCore.QRect(46, 470, 461, 61))
        self.ogr_edit_mail.setText("")
        self.ogr_edit_mail.setMaxLength(40)
        self.ogr_edit_mail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_edit_mail.setObjectName("ogr_edit_mail")
        self.ogr_edit_evAdresi = QtWidgets.QLineEdit(self.frame_4)
        self.ogr_edit_evAdresi.setGeometry(QtCore.QRect(563, 470, 461, 61))
        self.ogr_edit_evAdresi.setText("")
        self.ogr_edit_evAdresi.setMaxLength(40)
        self.ogr_edit_evAdresi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_edit_evAdresi.setObjectName("ogr_edit_evAdresi")
        self.btn_ogrenciDuzenle = QtWidgets.QPushButton(self.frame_4)
        self.btn_ogrenciDuzenle.setGeometry(QtCore.QRect(806, 561, 225, 64))
        self.btn_ogrenciDuzenle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciDuzenle.setStyleSheet("QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(64, 95, 208)\n"
"}")
        self.btn_ogrenciDuzenle.setObjectName("btn_ogrenciDuzenle")
        self.ogr_edit_telefon = QtWidgets.QLineEdit(self.frame_4)
        self.ogr_edit_telefon.setGeometry(QtCore.QRect(563, 390, 461, 61))
        self.ogr_edit_telefon.setText("")
        self.ogr_edit_telefon.setMaxLength(40)
        self.ogr_edit_telefon.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ogr_edit_telefon.setObjectName("ogr_edit_telefon")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(51, 70, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:36px;")
        self.label_8.setObjectName("label_8")
        self.ogr_edit_cinsiyet = QtWidgets.QComboBox(self.frame_4)
        self.ogr_edit_cinsiyet.setGeometry(QtCore.QRect(48, 550, 461, 61))
        self.ogr_edit_cinsiyet.setStyleSheet("font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.ogr_edit_cinsiyet.setObjectName("ogr_edit_cinsiyet")
        self.ogr_edit_cinsiyet.addItem("")
        self.ogr_edit_cinsiyet.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(56, 124, 691, 61))
        self.label_9.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_9.setObjectName("label_9")
        self.btn_ogrenciSil = QtWidgets.QPushButton(self.frame_4)
        self.btn_ogrenciSil.setGeometry(QtCore.QRect(564, 561, 225, 64))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_ogrenciSil.setFont(font)
        self.btn_ogrenciSil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciSil.setStyleSheet("QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(255, 66, 69)\n"
"}")
        self.btn_ogrenciSil.setObjectName("btn_ogrenciSil")
        self.combo_edit_classes = QtWidgets.QComboBox(self.frame_4)
        self.combo_edit_classes.setEnabled(True)
        self.combo_edit_classes.setGeometry(QtCore.QRect(60, 228, 271, 23))
        self.combo_edit_classes.setStyleSheet("font-size:15px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_edit_classes.setCurrentText("")
        self.combo_edit_classes.setObjectName("combo_edit_classes")
        self.combo_edit_learners = QtWidgets.QComboBox(self.frame_4)
        self.combo_edit_learners.setEnabled(True)
        self.combo_edit_learners.setGeometry(QtCore.QRect(347, 228, 271, 23))
        self.combo_edit_learners.setAutoFillBackground(False)
        self.combo_edit_learners.setStyleSheet("\n"
"font-size:15px;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"")
        self.combo_edit_learners.setEditable(False)
        self.combo_edit_learners.setCurrentText("")
        self.combo_edit_learners.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.combo_edit_learners.setDuplicatesEnabled(False)
        self.combo_edit_learners.setFrame(True)
        self.combo_edit_learners.setModelColumn(0)
        self.combo_edit_learners.setObjectName("combo_edit_learners")
        self.btn_ogrenciBilgileriGetir = QtWidgets.QPushButton(self.frame_4)
        self.btn_ogrenciBilgileriGetir.setGeometry(QtCore.QRect(630, 230, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_ogrenciBilgileriGetir.setFont(font)
        self.btn_ogrenciBilgileriGetir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciBilgileriGetir.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"}")
        self.btn_ogrenciBilgileriGetir.setObjectName("btn_ogrenciBilgileriGetir")
        self.label_7.raise_()
        self.label_13.raise_()
        self.label_16.raise_()
        self.frame_4.raise_()
        self.ogrenciStack.addWidget(self.qw_ogrenci_duzenle)
        self.qw_ogrenci_goruntule = QtWidgets.QWidget()
        self.qw_ogrenci_goruntule.setObjectName("qw_ogrenci_goruntule")
        self.label_12 = QtWidgets.QLabel(self.qw_ogrenci_goruntule)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.qw_ogrenci_goruntule)
        self.label_14.setGeometry(QtCore.QRect(73, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.qw_ogrenci_goruntule)
        self.label_17.setGeometry(QtCore.QRect(107, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_17.setObjectName("label_17")
        self.frame_7 = QtWidgets.QFrame(self.qw_ogrenci_goruntule)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 1075, 700))
        self.frame_7.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.2);\n"
"}\n"
"QLineEdit{\n"
"font-size:20px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}\n"
"QLineEdit:hover{\n"
"background:rgba(0,0,0,0.04);\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:silver;\n"
"background:transparent\n"
"}\n"
"QCheckBox:hover{\n"
"color:white;\n"
"}\n"
"QTextEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.btn_ogrenciYerlestir = QtWidgets.QPushButton(self.frame_7)
        self.btn_ogrenciYerlestir.setGeometry(QtCore.QRect(75, 300, 131, 41))
        self.btn_ogrenciYerlestir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciYerlestir.setStyleSheet("QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"font-size:17px\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(64, 95, 208)\n"
"}")
        self.btn_ogrenciYerlestir.setObjectName("btn_ogrenciYerlestir")
        self.label_41 = QtWidgets.QLabel(self.frame_7)
        self.label_41.setGeometry(QtCore.QRect(76, 70, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:26px;")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_7)
        self.label_42.setGeometry(QtCore.QRect(76, 111, 411, 51))
        self.label_42.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_42.setObjectName("label_42")
        self.combo_yerlestir_classes = QtWidgets.QComboBox(self.frame_7)
        self.combo_yerlestir_classes.setEnabled(True)
        self.combo_yerlestir_classes.setGeometry(QtCore.QRect(78, 180, 390, 41))
        self.combo_yerlestir_classes.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_yerlestir_classes.setCurrentText("")
        self.combo_yerlestir_classes.setObjectName("combo_yerlestir_classes")
        self.combo_yerlestir_learners = QtWidgets.QComboBox(self.frame_7)
        self.combo_yerlestir_learners.setEnabled(True)
        self.combo_yerlestir_learners.setGeometry(QtCore.QRect(78, 240, 390, 41))
        self.combo_yerlestir_learners.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_yerlestir_learners.setCurrentText("")
        self.combo_yerlestir_learners.setObjectName("combo_yerlestir_learners")
        self.label_yerlestir_class = QtWidgets.QLabel(self.frame_7)
        self.label_yerlestir_class.setGeometry(QtCore.QRect(215, 299, 301, 21))
        self.label_yerlestir_class.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_yerlestir_class.setText("")
        self.label_yerlestir_class.setObjectName("label_yerlestir_class")
        self.label_yerlestir_learners = QtWidgets.QLabel(self.frame_7)
        self.label_yerlestir_learners.setGeometry(QtCore.QRect(215, 320, 301, 21))
        self.label_yerlestir_learners.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_yerlestir_learners.setText("")
        self.label_yerlestir_learners.setObjectName("label_yerlestir_learners")
        self.btn_ogrenciDersKaydi = QtWidgets.QPushButton(self.frame_7)
        self.btn_ogrenciDersKaydi.setGeometry(QtCore.QRect(585, 300, 131, 41))
        self.btn_ogrenciDersKaydi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciDersKaydi.setStyleSheet("QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"font-size:17px\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(64, 95, 208)\n"
"}")
        self.btn_ogrenciDersKaydi.setObjectName("btn_ogrenciDersKaydi")
        self.label_43 = QtWidgets.QLabel(self.frame_7)
        self.label_43.setGeometry(QtCore.QRect(586, 111, 411, 51))
        self.label_43.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_43.setObjectName("label_43")
        self.label_kayit_lessons = QtWidgets.QLabel(self.frame_7)
        self.label_kayit_lessons.setGeometry(QtCore.QRect(725, 299, 301, 21))
        self.label_kayit_lessons.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_kayit_lessons.setObjectName("label_kayit_lessons")
        self.combo_kayit_learners = QtWidgets.QComboBox(self.frame_7)
        self.combo_kayit_learners.setEnabled(True)
        self.combo_kayit_learners.setGeometry(QtCore.QRect(588, 240, 390, 41))
        self.combo_kayit_learners.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_kayit_learners.setCurrentText("")
        self.combo_kayit_learners.setObjectName("combo_kayit_learners")
        self.combo_kayit_lessons = QtWidgets.QComboBox(self.frame_7)
        self.combo_kayit_lessons.setEnabled(True)
        self.combo_kayit_lessons.setGeometry(QtCore.QRect(588, 180, 390, 41))
        self.combo_kayit_lessons.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_kayit_lessons.setCurrentText("")
        self.combo_kayit_lessons.setObjectName("combo_kayit_lessons")
        self.label_44 = QtWidgets.QLabel(self.frame_7)
        self.label_44.setGeometry(QtCore.QRect(586, 70, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:26px;")
        self.label_44.setObjectName("label_44")
        self.label_kayit_learners = QtWidgets.QLabel(self.frame_7)
        self.label_kayit_learners.setGeometry(QtCore.QRect(725, 320, 301, 21))
        self.label_kayit_learners.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_kayit_learners.setObjectName("label_kayit_learners")
        self.label_yerlestir_learners_2 = QtWidgets.QLabel(self.frame_7)
        self.label_yerlestir_learners_2.setGeometry(QtCore.QRect(190, 630, 301, 21))
        self.label_yerlestir_learners_2.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_yerlestir_learners_2.setText("")
        self.label_yerlestir_learners_2.setObjectName("label_yerlestir_learners_2")
        self.label_45 = QtWidgets.QLabel(self.frame_7)
        self.label_45.setGeometry(QtCore.QRect(76, 421, 411, 51))
        self.label_45.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_45.setObjectName("label_45")
        self.btn_ogrenciDuzenle_4 = QtWidgets.QPushButton(self.frame_7)
        self.btn_ogrenciDuzenle_4.setGeometry(QtCore.QRect(75, 610, 131, 41))
        self.btn_ogrenciDuzenle_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciDuzenle_4.setStyleSheet("QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"font-size:17px\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(64, 95, 208)\n"
"}")
        self.btn_ogrenciDuzenle_4.setObjectName("btn_ogrenciDuzenle_4")
        self.label_yerlestir_class_2 = QtWidgets.QLabel(self.frame_7)
        self.label_yerlestir_class_2.setGeometry(QtCore.QRect(190, 609, 301, 21))
        self.label_yerlestir_class_2.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_yerlestir_class_2.setText("")
        self.label_yerlestir_class_2.setObjectName("label_yerlestir_class_2")
        self.combo_yerlestir_learners_2 = QtWidgets.QComboBox(self.frame_7)
        self.combo_yerlestir_learners_2.setEnabled(True)
        self.combo_yerlestir_learners_2.setGeometry(QtCore.QRect(78, 550, 390, 41))
        self.combo_yerlestir_learners_2.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_yerlestir_learners_2.setCurrentText("")
        self.combo_yerlestir_learners_2.setObjectName("combo_yerlestir_learners_2")
        self.combo_yerlestir_classes_2 = QtWidgets.QComboBox(self.frame_7)
        self.combo_yerlestir_classes_2.setEnabled(True)
        self.combo_yerlestir_classes_2.setGeometry(QtCore.QRect(78, 490, 390, 41))
        self.combo_yerlestir_classes_2.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_yerlestir_classes_2.setCurrentText("")
        self.combo_yerlestir_classes_2.setObjectName("combo_yerlestir_classes_2")
        self.label_46 = QtWidgets.QLabel(self.frame_7)
        self.label_46.setGeometry(QtCore.QRect(76, 380, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:26px;")
        self.label_46.setObjectName("label_46")
        self.label_kayit_learners_2 = QtWidgets.QLabel(self.frame_7)
        self.label_kayit_learners_2.setGeometry(QtCore.QRect(700, 630, 301, 21))
        self.label_kayit_learners_2.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_kayit_learners_2.setText("")
        self.label_kayit_learners_2.setObjectName("label_kayit_learners_2")
        self.combo_kayit_learners_2 = QtWidgets.QComboBox(self.frame_7)
        self.combo_kayit_learners_2.setEnabled(True)
        self.combo_kayit_learners_2.setGeometry(QtCore.QRect(588, 550, 390, 41))
        self.combo_kayit_learners_2.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_kayit_learners_2.setCurrentText("")
        self.combo_kayit_learners_2.setObjectName("combo_kayit_learners_2")
        self.label_kayit_lessons_2 = QtWidgets.QLabel(self.frame_7)
        self.label_kayit_lessons_2.setGeometry(QtCore.QRect(700, 609, 301, 21))
        self.label_kayit_lessons_2.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:14px;")
        self.label_kayit_lessons_2.setText("")
        self.label_kayit_lessons_2.setObjectName("label_kayit_lessons_2")
        self.label_47 = QtWidgets.QLabel(self.frame_7)
        self.label_47.setGeometry(QtCore.QRect(586, 380, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("background:transparent;\n"
"color:rgb(195, 195, 195);\n"
"font-size:26px;")
        self.label_47.setObjectName("label_47")
        self.combo_kayit_lessons_2 = QtWidgets.QComboBox(self.frame_7)
        self.combo_kayit_lessons_2.setEnabled(True)
        self.combo_kayit_lessons_2.setGeometry(QtCore.QRect(588, 490, 390, 41))
        self.combo_kayit_lessons_2.setStyleSheet("font-size:20px;;\n"
"color:rgb(195, 195, 195);\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;")
        self.combo_kayit_lessons_2.setCurrentText("")
        self.combo_kayit_lessons_2.setObjectName("combo_kayit_lessons_2")
        self.label_48 = QtWidgets.QLabel(self.frame_7)
        self.label_48.setGeometry(QtCore.QRect(586, 421, 411, 51))
        self.label_48.setStyleSheet("background:transparent;\n"
"color:silver;\n"
"border:none;\n"
"font-size:15px;")
        self.label_48.setObjectName("label_48")
        self.btn_ogrenciDuzenle_5 = QtWidgets.QPushButton(self.frame_7)
        self.btn_ogrenciDuzenle_5.setGeometry(QtCore.QRect(585, 610, 131, 41))
        self.btn_ogrenciDuzenle_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenciDuzenle_5.setStyleSheet("QPushButton{\n"
"background:rgb(79, 117, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"font-size:17px\n"
"}\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(64, 95, 208)\n"
"}")
        self.btn_ogrenciDuzenle_5.setObjectName("btn_ogrenciDuzenle_5")
        self.btn_ogrenciYerlestir.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.combo_yerlestir_classes.raise_()
        self.combo_yerlestir_learners.raise_()
        self.label_yerlestir_class.raise_()
        self.label_yerlestir_learners.raise_()
        self.btn_ogrenciDersKaydi.raise_()
        self.label_43.raise_()
        self.label_kayit_lessons.raise_()
        self.combo_kayit_learners.raise_()
        self.combo_kayit_lessons.raise_()
        self.label_44.raise_()
        self.label_kayit_learners.raise_()
        self.label_yerlestir_learners_2.raise_()
        self.label_45.raise_()
        self.btn_ogrenciDuzenle_4.raise_()
        self.label_yerlestir_class_2.raise_()
        self.combo_yerlestir_learners_2.raise_()
        self.combo_yerlestir_classes_2.raise_()
        self.label_46.raise_()
        self.label_kayit_learners_2.raise_()
        self.combo_kayit_learners_2.raise_()
        self.label_kayit_lessons_2.raise_()
        self.label_47.raise_()
        self.combo_kayit_lessons_2.raise_()
        self.label_48.raise_()
        self.btn_ogrenciDuzenle_5.raise_()
        self.ogrenciStack.addWidget(self.qw_ogrenci_goruntule)
        self.mainStack.addWidget(self.qw_ogrenci)
        self.qw_yoklama = QtWidgets.QWidget()
        self.qw_yoklama.setObjectName("qw_yoklama")
        self.yoklamaNotStack = QtWidgets.QStackedWidget(self.qw_yoklama)
        self.yoklamaNotStack.setGeometry(QtCore.QRect(0, 0, 1075, 700))
        self.yoklamaNotStack.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.97);\n"
"border:none;\n"
"color:white;\n"
"}")
        self.yoklamaNotStack.setObjectName("yoklamaNotStack")
        self.qw_yoklama_al = QtWidgets.QWidget()
        self.qw_yoklama_al.setObjectName("qw_yoklama_al")
        self.label_27 = QtWidgets.QLabel(self.qw_yoklama_al)
        self.label_27.setGeometry(QtCore.QRect(105, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.qw_yoklama_al)
        self.label_28.setGeometry(QtCore.QRect(20, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_28.setObjectName("label_28")
        self.label_32 = QtWidgets.QLabel(self.qw_yoklama_al)
        self.label_32.setGeometry(QtCore.QRect(139, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_32.setObjectName("label_32")
        self.yoklamaNotStack.addWidget(self.qw_yoklama_al)
        self.qw_not_gir = QtWidgets.QWidget()
        self.qw_not_gir.setObjectName("qw_not_gir")
        self.label_29 = QtWidgets.QLabel(self.qw_not_gir)
        self.label_29.setGeometry(QtCore.QRect(20, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.qw_not_gir)
        self.label_30.setGeometry(QtCore.QRect(105, 13, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.qw_not_gir)
        self.label_31.setGeometry(QtCore.QRect(139, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("QLabel{\n"
"color:silver;\n"
"background:transparent;\n"
"}")
        self.label_31.setObjectName("label_31")
        self.yoklamaNotStack.addWidget(self.qw_not_gir)
        self.mainStack.addWidget(self.qw_yoklama)
        self.qw_hesap = QtWidgets.QWidget()
        self.qw_hesap.setObjectName("qw_hesap")
        self.label_6 = QtWidgets.QLabel(self.qw_hesap)
        self.label_6.setGeometry(QtCore.QRect(210, 20, 381, 131))
        self.label_6.setStyleSheet("color: white;\n"
"font-size:40px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.mainStack.addWidget(self.qw_hesap)
        self.hesapWidget = QtWidgets.QWidget(self.frame)
        self.hesapWidget.setGeometry(QtCore.QRect(1095, 100, 155, 41))
        self.hesapWidget.setStyleSheet("QPushButton{\n"
"background:rgba(101,52,172,0.93);border:none;color:white;font-size:28px;\n"
"}\n"
"QWidget{\n"
"background:rgba(53, 63, 89,0.9);\n"
"}")
        self.hesapWidget.setObjectName("hesapWidget")
        self.btn_hesap_setting = QtWidgets.QPushButton(self.hesapWidget)
        self.btn_hesap_setting.setGeometry(QtCore.QRect(0, 0, 155, 41))
        self.btn_hesap_setting.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_hesap_setting.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.btn_hesap_setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_hesap_setting.setStyleSheet("\n"
"QPushButton{\n"
"background:rgba(45,54,76,0.93);\n"
"border:none;\n"
"color:silver;\n"
"font-size:17px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(40,49,71,0.97);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}")
        self.btn_hesap_setting.setObjectName("btn_hesap_setting")
        self.menuStack = QtWidgets.QStackedWidget(self.frame)
        self.menuStack.setGeometry(QtCore.QRect(175, 100, 175, 700))
        self.menuStack.setMinimumSize(QtCore.QSize(175, 700))
        self.menuStack.setMaximumSize(QtCore.QSize(1075, 700))
        self.menuStack.setStyleSheet("QWidget{\n"
"background:transparent\n"
"}\n"
"")
        self.menuStack.setObjectName("menuStack")
        self.menu_ogrenci = QtWidgets.QWidget()
        self.menu_ogrenci.setObjectName("menu_ogrenci")
        self.btn_ogrenci_ekle = QtWidgets.QPushButton(self.menu_ogrenci)
        self.btn_ogrenci_ekle.setGeometry(QtCore.QRect(0, 170, 175, 57))
        self.btn_ogrenci_ekle.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ogrenci_ekle.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ogrenci_ekle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenci_ekle.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_ogrenci_ekle.setObjectName("btn_ogrenci_ekle")
        self.btn_ogrenci_duzenle = QtWidgets.QPushButton(self.menu_ogrenci)
        self.btn_ogrenci_duzenle.setGeometry(QtCore.QRect(0, 227, 175, 57))
        self.btn_ogrenci_duzenle.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ogrenci_duzenle.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ogrenci_duzenle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenci_duzenle.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_ogrenci_duzenle.setObjectName("btn_ogrenci_duzenle")
        self.btn_ogrenci_goruntule = QtWidgets.QPushButton(self.menu_ogrenci)
        self.btn_ogrenci_goruntule.setGeometry(QtCore.QRect(0, 284, 175, 56))
        self.btn_ogrenci_goruntule.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ogrenci_goruntule.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ogrenci_goruntule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogrenci_goruntule.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_ogrenci_goruntule.setObjectName("btn_ogrenci_goruntule")
        self.menuStack.addWidget(self.menu_ogrenci)
        self.menu_ders = QtWidgets.QWidget()
        self.menu_ders.setObjectName("menu_ders")
        self.btn_ders_goruntule = QtWidgets.QPushButton(self.menu_ders)
        self.btn_ders_goruntule.setGeometry(QtCore.QRect(0, 453, 175, 57))
        self.btn_ders_goruntule.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ders_goruntule.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ders_goruntule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ders_goruntule.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_ders_goruntule.setObjectName("btn_ders_goruntule")
        self.btn_ders_duzenle = QtWidgets.QPushButton(self.menu_ders)
        self.btn_ders_duzenle.setGeometry(QtCore.QRect(0, 397, 175, 56))
        self.btn_ders_duzenle.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ders_duzenle.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ders_duzenle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ders_duzenle.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_ders_duzenle.setObjectName("btn_ders_duzenle")
        self.btn_ders_ekle = QtWidgets.QPushButton(self.menu_ders)
        self.btn_ders_ekle.setGeometry(QtCore.QRect(0, 340, 175, 57))
        self.btn_ders_ekle.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_ders_ekle.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_ders_ekle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ders_ekle.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_ders_ekle.setObjectName("btn_ders_ekle")
        self.menuStack.addWidget(self.menu_ders)
        self.menu_yoklama_not = QtWidgets.QWidget()
        self.menu_yoklama_not.setObjectName("menu_yoklama_not")
        self.btn_yoklama_al = QtWidgets.QPushButton(self.menu_yoklama_not)
        self.btn_yoklama_al.setGeometry(QtCore.QRect(0, 510, 175, 85))
        self.btn_yoklama_al.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_yoklama_al.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_yoklama_al.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_yoklama_al.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_yoklama_al.setObjectName("btn_yoklama_al")
        self.btn_not_gir = QtWidgets.QPushButton(self.menu_yoklama_not)
        self.btn_not_gir.setGeometry(QtCore.QRect(0, 595, 175, 85))
        self.btn_not_gir.setMinimumSize(QtCore.QSize(175, 0))
        self.btn_not_gir.setMaximumSize(QtCore.QSize(175, 16777215))
        self.btn_not_gir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_not_gir.setStyleSheet("QPushButton{\n"
"background:rgba(45,54,76,0.99);\n"
"border:none;\n"
"color:silver;\n"
"font-size:18px;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(35,43,62,0.99);\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid rgb(38,46,65)\n"
"}\n"
"")
        self.btn_not_gir.setObjectName("btn_not_gir")
        self.menuStack.addWidget(self.menu_yoklama_not)
        self.gorevCubugu.raise_()
        self.btn_ogrenci.raise_()
        self.btn_ders.raise_()
        self.btn_yoklama_not.raise_()
        self.btn_profil.raise_()
        self.mainStack.raise_()
        self.hesapWidget.raise_()
        self.menuStack.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1250, 40))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.45);\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background:rgba(0,0,0,0.50);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:silver;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(14, 5, 21, 31))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(41, 11, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:silver;\n"
"background:transparent;")
        self.label_2.setObjectName("label_2")
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setGeometry(QtCore.QRect(1211, 0, 41, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.15);\n"
"color:silver;\n"
"\n"
"border-radius:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background:red;\n"
"color:white\n"
"}")
        self.btn_close.setObjectName("btn_close")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_2)
        self.btn_minimize.setGeometry(QtCore.QRect(1170, 0, 41, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.15);\n"
"border-radius:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(0, 0, 0,0.6)\n"
"}")
        self.btn_minimize.setObjectName("btn_minimize")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainStack.setCurrentIndex(0)
        self.dersStack.setCurrentIndex(0)
        self.ogrenciStack.setCurrentIndex(2)
        self.ogr_edit_cinsiyet.setCurrentIndex(0)
        self.combo_edit_learners.setCurrentIndex(-1)
        self.yoklamaNotStack.setCurrentIndex(1)
        self.menuStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Öğrenci Takip Sİstemi"))
        self.btn_profil.setText(_translate("MainWindow", "PROFİL"))
        self.label_department_name.setText(_translate("MainWindow", "BÖLÜM İSMİ"))
        self.btn_hesap.setText(_translate("MainWindow", "HESAP"))
        self.label_username.setText(_translate("MainWindow", "KULLANICI ADI"))
        self.btn_ogrenci.setText(_translate("MainWindow", "ÖĞRENCİ"))
        self.btn_ders.setText(_translate("MainWindow", "DERS\n"
"SINIF"))
        self.btn_yoklama_not.setText(_translate("MainWindow", "\n"
"YOKLAMA\n"
"NOT"))
        self.label_18.setText(_translate("MainWindow", "Ders - Sınıf"))
        self.label_19.setText(_translate("MainWindow", " ⇢"))
        self.label_24.setText(_translate("MainWindow", "Ders -Sınıf Ekle"))
        self.ders_ekle_kod.setPlaceholderText(_translate("MainWindow", "Ders Kodu"))
        self.ders_ekle_isim.setPlaceholderText(_translate("MainWindow", "Ders İsmi"))
        self.btn_dersEkle.setText(_translate("MainWindow", "Ders Ekle"))
        self.btn_dersEkle.setShortcut(_translate("MainWindow", "Return"))
        self.label_11.setText(_translate("MainWindow", "DERS EKLEME İŞLEMİ"))
        self.label_33.setText(_translate("MainWindow", "Ders eklemek için aşağıdaki alanları eksiksiz bir şekilde doldurup \n"
"\'Ders Ekle\' Butonuna basınız"))
        self.ders_ekle_tanim.setPlaceholderText(_translate("MainWindow", "Ders Tanımı"))
        self.ders_ekle_akts.setPlaceholderText(_translate("MainWindow", "Ders AKTS"))
        self.ders_ekle_kredi.setPlaceholderText(_translate("MainWindow", "Ders KREDİ"))
        self.ders_ekle_finalYuzde.setPlaceholderText(_translate("MainWindow", "Final Yüzdesi"))
        self.ders_ekle_vizeYuzde.setPlaceholderText(_translate("MainWindow", "Vize Yüzdesi"))
        self.label_34.setText(_translate("MainWindow", "Sınıf eklemek için aşağıdaki alanları eksiksiz bir şekilde doldurup \n"
"\'Sınıf Ekle\' Butonuna basınız"))
        self.label_35.setText(_translate("MainWindow", "SINIF EKLEME İŞLEMİ"))
        self.sinif_ekle_kod.setPlaceholderText(_translate("MainWindow", "Sınıf Kodu"))
        self.sinif_ekle_isim.setPlaceholderText(_translate("MainWindow", "Sınıf İsmi"))
        self.btn_sinifEkle.setText(_translate("MainWindow", "Sınıf Ekle"))
        self.btn_sinifEkle.setShortcut(_translate("MainWindow", "Return"))
        self.label_40.setText(_translate("MainWindow", "BANNER HERE :)"))
        self.label_20.setText(_translate("MainWindow", " ⇢"))
        self.label_21.setText(_translate("MainWindow", "Ders"))
        self.label_25.setText(_translate("MainWindow", "Ders Düzenle"))
        self.label_22.setText(_translate("MainWindow", " ⇢"))
        self.label_23.setText(_translate("MainWindow", "Ders"))
        self.label_26.setText(_translate("MainWindow", "Ders Görüntüle"))
        self.label_4.setText(_translate("MainWindow", "Öğrenci  "))
        self.label_10.setText(_translate("MainWindow", " ⇢"))
        self.label_15.setText(_translate("MainWindow", "Öğrenci Ekle  "))
        self.ogr_ekle_ad.setPlaceholderText(_translate("MainWindow", "Öğrenci Adı"))
        self.ogr_ekle_soyad.setPlaceholderText(_translate("MainWindow", "Öğrenci Soyadı"))
        self.ogr_ekle_dogumTarhi.setPlaceholderText(_translate("MainWindow", "Öğrenci Doğum Tarihi (01.01.2019)"))
        self.ogr_ekle_mail.setPlaceholderText(_translate("MainWindow", "Öğrenci Mail Adresi"))
        self.ogr_ekle_evAdresi.setPlaceholderText(_translate("MainWindow", "Öğrenci Ev Adresi"))
        self.btn_ogrenciEkle.setText(_translate("MainWindow", "Öğrenci Ekle"))
        self.btn_ogrenciEkle.setShortcut(_translate("MainWindow", "Return"))
        self.ogr_ekle_telefon.setPlaceholderText(_translate("MainWindow", "Telefon Numarası (0537 841 5477)"))
        self.label.setText(_translate("MainWindow", "ÖĞRENCİ EKLEME İŞLEMİ"))
        self.ogr_ekle_cinsiyet.setCurrentText(_translate("MainWindow", "Erkek"))
        self.ogr_ekle_cinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.ogr_ekle_cinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_5.setText(_translate("MainWindow", "Öğrenci eklemek için aşağıdaki alanları eksiksiz bir şekilde doldurup \n"
"\'Öğrenci Ekle\' Butonuna basınız"))
        self.ogr_ekle_okulNumarasi.setPlaceholderText(_translate("MainWindow", "Öğrenci Okul Numarası"))
        self.label_13.setText(_translate("MainWindow", " ⇢"))
        self.label_7.setText(_translate("MainWindow", "Öğrenci"))
        self.label_16.setText(_translate("MainWindow", "Öğrenci Düzenle"))
        self.ogr_edit_ad.setPlaceholderText(_translate("MainWindow", "Öğrenci Adı"))
        self.ogr_edit_soyad.setPlaceholderText(_translate("MainWindow", "Öğrenci Soyadı"))
        self.ogr_edit_dogumTarihi.setPlaceholderText(_translate("MainWindow", "Öğrenci Doğum Tarihi (01.01.2019)"))
        self.ogr_edit_mail.setPlaceholderText(_translate("MainWindow", "Öğrenci Mail Adresi"))
        self.ogr_edit_evAdresi.setPlaceholderText(_translate("MainWindow", "Öğrenci Ev Adresi"))
        self.btn_ogrenciDuzenle.setText(_translate("MainWindow", "Öğrenci Düzenle"))
        self.btn_ogrenciDuzenle.setShortcut(_translate("MainWindow", "Return"))
        self.ogr_edit_telefon.setPlaceholderText(_translate("MainWindow", "Öğrenci Telefon Numarası"))
        self.label_8.setText(_translate("MainWindow", "ÖĞRENCİ DÜZENLEME İŞLEMİ"))
        self.ogr_edit_cinsiyet.setCurrentText(_translate("MainWindow", "Erkek"))
        self.ogr_edit_cinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.ogr_edit_cinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_9.setText(_translate("MainWindow", "Öğrenci düzenlemek için öğrenci seç bölümünden öğrenci seçip \'BİLGİLERİ GETİR\' e bastıktan sonra, \n"
"öğrenci bilgileri üzerinde değişiklik yapıp \'Öğrenci Düzenle\' butonuna basınız.   \n"
"\'Belirli bir öğrenciyi arıyorsanız, sınıf seçebilirsiniz."))
        self.btn_ogrenciSil.setText(_translate("MainWindow", "Öğrenci Sil"))
        self.btn_ogrenciSil.setShortcut(_translate("MainWindow", "Return"))
        self.btn_ogrenciBilgileriGetir.setText(_translate("MainWindow", "BİLGİLERİ GETİR"))
        self.btn_ogrenciBilgileriGetir.setShortcut(_translate("MainWindow", "Return"))
        self.label_12.setText(_translate("MainWindow", "Öğrenci "))
        self.label_14.setText(_translate("MainWindow", " ⇢"))
        self.label_17.setText(_translate("MainWindow", "Öğrenci Ders-Sınıf Kaydı"))
        self.btn_ogrenciYerlestir.setText(_translate("MainWindow", "Yerleştir"))
        self.btn_ogrenciYerlestir.setShortcut(_translate("MainWindow", "Return"))
        self.label_41.setText(_translate("MainWindow", "ÖĞRENCİYİ SINIFA YERLEŞTİRME"))
        self.label_42.setText(_translate("MainWindow", "Herhangi bir öğrenciyi bir sınıfa yerleştirmek için sınıf seçimi\n"
"yaptıktan sonra öğrenci seçip \'Yerleştir\' butonuna tıklayınız."))
        self.btn_ogrenciDersKaydi.setText(_translate("MainWindow", "Ders Kaydet"))
        self.btn_ogrenciDersKaydi.setShortcut(_translate("MainWindow", "Return"))
        self.label_43.setText(_translate("MainWindow", "Herhangi bir öğrenciye ders kaydı yapabilmek için\n"
"Öncelikle öğrenciyi bir sınıfa yerleştirmeniz gerekmektedir"))
        self.label_kayit_lessons.setText(_translate("MainWindow", "Bilgisayar Programcılığı"))
        self.label_44.setText(_translate("MainWindow", "DERS KAYDI"))
        self.label_kayit_learners.setText(_translate("MainWindow", "Bilgisayar Programcılığı"))
        self.label_45.setText(_translate("MainWindow", "Herhangi bir öğrenciyi mezun etmek için sınıf seçimii\n"
"yaptıktan sonra öğrenci seçip \'Mezun Et\' butonuna tıklayınız."))
        self.btn_ogrenciDuzenle_4.setText(_translate("MainWindow", "Mezun Et"))
        self.btn_ogrenciDuzenle_4.setShortcut(_translate("MainWindow", "Return"))
        self.label_46.setText(_translate("MainWindow", "ÖĞRENCİYİ MEZUN ET"))
        self.label_47.setText(_translate("MainWindow", "DERSİ KALDIR"))
        self.label_48.setText(_translate("MainWindow", "Herhangi bir öğrenicden ders kaldırmak için ders seçimi\n"
"yaptıktan sonra öğrenci seçip \'Ders Kaldır\' butonuna tıklayınız."))
        self.btn_ogrenciDuzenle_5.setText(_translate("MainWindow", "Ders Kaldır"))
        self.btn_ogrenciDuzenle_5.setShortcut(_translate("MainWindow", "Return"))
        self.label_27.setText(_translate("MainWindow", " ⇢"))
        self.label_28.setText(_translate("MainWindow", "Yoklama Not"))
        self.label_32.setText(_translate("MainWindow", "Yoklama Al"))
        self.label_29.setText(_translate("MainWindow", "Yoklama Not"))
        self.label_30.setText(_translate("MainWindow", " ⇢"))
        self.label_31.setText(_translate("MainWindow", "Not Gir"))
        self.label_6.setText(_translate("MainWindow", "HESAP AYARLARI"))
        self.btn_hesap_setting.setText(_translate("MainWindow", "Hesap Ayarları"))
        self.btn_ogrenci_ekle.setText(_translate("MainWindow", "Ö. EKLE"))
        self.btn_ogrenci_duzenle.setText(_translate("MainWindow", "Ö. DÜZENLE"))
        self.btn_ogrenci_goruntule.setText(_translate("MainWindow", "ÖĞRENCİ \n"
"DERS-SINIF KAYDI"))
        self.btn_ders_goruntule.setText(_translate("MainWindow", "DERS - SINIF\n"
"GÖRÜNTÜLE"))
        self.btn_ders_duzenle.setText(_translate("MainWindow", "DERS - SINIF\n"
"DÜZENLE"))
        self.btn_ders_ekle.setText(_translate("MainWindow", "DERS - SINIF\n"
"EKLE"))
        self.btn_yoklama_al.setText(_translate("MainWindow", "YOKLAMA AL"))
        self.btn_not_gir.setText(_translate("MainWindow", "NOT GİR"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":images/images/yu_ana_logo2.png\" width=\"21\" height=\"30\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Öğrenci Takip Sistemi"))
        self.btn_close.setText(_translate("MainWindow", "✕"))
        self.btn_minimize.setText(_translate("MainWindow", "_"))

import images_rc
