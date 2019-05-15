# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lenovo\Desktop\PYTHON OTOMOSYON\design\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(462, 544)
        Login.setMinimumSize(QtCore.QSize(462, 544))
        Login.setMaximumSize(QtCore.QSize(462, 544))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/yu_Icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("#Login{\n"
"background:url(:/images/images/ballon.jpg);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(0,0,0,0.7);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background:rgba(0,0,0,0.73);\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background:rgba(0,0,0,0.04);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background:rgb(83, 152, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(68, 117, 222)\n"
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
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(21, 80, 420, 440))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(20, 161, 371, 61))
        self.username.setText("")
        self.username.setMaxLength(24)
        self.username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username.setCursorPosition(0)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(20, 241, 371, 61))
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.baslik = QtWidgets.QLabel(self.frame)
        self.baslik.setGeometry(QtCore.QRect(20, 80, 391, 71))
        self.baslik.setStyleSheet("font-size:40px;\n"
"color:white;\n"
"background:transparent;")
        self.baslik.setObjectName("baslik")
        self.baslik_2 = QtWidgets.QLabel(self.frame)
        self.baslik_2.setGeometry(QtCore.QRect(81, 45, 321, 21))
        self.baslik_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.baslik_2.setStyleSheet("font-size:18px;\n"
"color:white;\n"
"background:transparent;")
        self.baslik_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.baslik_2.setTextFormat(QtCore.Qt.AutoText)
        self.baslik_2.setScaledContents(False)
        self.baslik_2.setOpenExternalLinks(True)
        self.baslik_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.baslik_2.setObjectName("baslik_2")
        self.remember_me = QtWidgets.QCheckBox(self.frame)
        self.remember_me.setGeometry(QtCore.QRect(20, 318, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remember_me.setFont(font)
        self.remember_me.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remember_me.setStyleSheet("")
        self.remember_me.setObjectName("remember_me")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(150, 320, 1, 18))
        self.line.setStyleSheet("background:white;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_sign = QtWidgets.QPushButton(self.frame)
        self.btn_sign.setGeometry(QtCore.QRect(30, 353, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_sign.setFont(font)
        self.btn_sign.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_newAccount = QtWidgets.QPushButton(self.frame)
        self.btn_newAccount.setGeometry(QtCore.QRect(170, 318, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_newAccount.setFont(font)
        self.btn_newAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_newAccount.setStyleSheet("QPushButton{\n"
"background:transparent\n"
"}\n"
"\n"
"QPushButton{\n"
"color:silver;\n"
"background:transparent\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"}\n"
"\n"
"")
        self.btn_newAccount.setObjectName("btn_newAccount")
        self.baslik.raise_()
        self.username.raise_()
        self.password.raise_()
        self.baslik_2.raise_()
        self.remember_me.raise_()
        self.line.raise_()
        self.btn_sign.raise_()
        self.btn_newAccount.raise_()
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(53, 43, 71, 111))
        self.label.setStyleSheet("background:none;")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Login)
        self.frame_2.setGeometry(QtCore.QRect(-2, 0, 471, 38))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.38);\n"
"}\n"
"QFrame{\n"
"border-radius:none;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background:rgba(0,0,0,0.40);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(14, 3, 21, 31))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 12, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:silver;\n"
"background:transparent;")
        self.label_2.setObjectName("label_2")
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setGeometry(QtCore.QRect(424, 0, 41, 38))
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
        self.btn_minimize.setGeometry(QtCore.QRect(383, 0, 41, 38))
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
        self.frame_2.raise_()
        self.frame.raise_()
        self.label.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "ÖTS - Giriş"))
        self.username.setPlaceholderText(_translate("Login", "Kullanıcı Adı"))
        self.password.setPlaceholderText(_translate("Login", "Şifre"))
        self.baslik.setText(_translate("Login", "Öğrenci Takip Sistemi"))
        self.baslik_2.setText(_translate("Login", "Y A L O V A   Ü N İ V E R S İ T E S İ"))
        self.remember_me.setText(_translate("Login", "Beni Hatırla"))
        self.btn_sign.setText(_translate("Login", "Giriş Yap"))
        self.btn_newAccount.setText(_translate("Login", "Yeni Hesap Oluştur"))
        self.label.setText(_translate("Login", "<html><head/><body><p><img src=\":/images/images/yu_ana_logo2.png\" width=\"67\" height=\"105\"/></p></body></html>"))
        self.label_3.setText(_translate("Login", "<html><head/><body><p><img src=\":images/images/yu_ana_logo2.png\" width=\"21\" height=\"30\"/></p></body></html>"))
        self.label_2.setText(_translate("Login", "Giriş Yap"))
        self.btn_close.setText(_translate("Login", "✕"))
        self.btn_minimize.setText(_translate("Login", "_"))

import images_rc
