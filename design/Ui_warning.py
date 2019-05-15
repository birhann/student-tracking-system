# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lenovo\Desktop\PYTHON OTOMOSYON\design\warning.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_warning(object):
    def setupUi(self, warning):
        warning.setObjectName("warning")
        warning.resize(320, 200)
        warning.setMinimumSize(QtCore.QSize(320, 200))
        warning.setMaximumSize(QtCore.QSize(320, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/yu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        warning.setWindowIcon(icon)
        warning.setStyleSheet("")
        self.frame_2 = QtWidgets.QFrame(warning)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 320, 38))
        self.frame_2.setMinimumSize(QtCore.QSize(320, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(320, 16777215))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.1);\n"
"}\n"
"QFrame{\n"
"border-radius:none;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background:rgba(0,0,0,0.2);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(14, 3, 21, 31))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(42, 9, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:white;\n"
"background:transparent;")
        self.label_2.setObjectName("label_2")
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setGeometry(QtCore.QRect(279, 0, 41, 38))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.01);\n"
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
        self.frame_3 = QtWidgets.QFrame(warning)
        self.frame_3.setGeometry(QtCore.QRect(0, 150, 341, 51))
        self.frame_3.setStyleSheet("background:white;\n"
"QPushButton{\n"
"background:rgb(83, 152, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(68, 117, 222)\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_tamam = QtWidgets.QPushButton(self.frame_3)
        self.btn_tamam.setGeometry(QtCore.QRect(197, 8, 111, 35))
        self.btn_tamam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_tamam.setStyleSheet("\n"
"QPushButton{\n"
"background:#c2b448;\n"
"border-radius:3px;\n"
"color:rgb(240, 240, 240);\n"
"font-size:18px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#9f923a;\n"
"color:white;\n"
"font-size:19px;\n"
" }")
        self.btn_tamam.setObjectName("btn_tamam")
        self.frame = QtWidgets.QFrame(warning)
        self.frame.setGeometry(QtCore.QRect(-5, -8, 335, 161))
        self.frame.setStyleSheet("QFrame{\n"
"background:url(:/images/images/warning_back2.png);\n"
"}\n"
"QFrame:hover{\n"
"background:#9c8d39;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(86, 54, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color:white;\n"
"background:transparent;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(34, 41, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"color:white;\n"
"background:transparent;")
        self.label_7.setObjectName("label_7")
        self.txt_error = QtWidgets.QPlainTextEdit(self.frame)
        self.txt_error.setEnabled(False)
        self.txt_error.setGeometry(QtCore.QRect(32, 92, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_error.setFont(font)
        self.txt_error.setStyleSheet("QPlainTextEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:white;}\n"
"\n"
"QPlainTextEdit:hover{\n"
"color:white;\n"
"}")
        self.txt_error.setObjectName("txt_error")
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()

        self.retranslateUi(warning)
        QtCore.QMetaObject.connectSlotsByName(warning)

    def retranslateUi(self, warning):
        _translate = QtCore.QCoreApplication.translate
        warning.setWindowTitle(_translate("warning", "Uyarı"))
        self.label_3.setText(_translate("warning", "<html><head/><body><p><img src=\":/images/images/yu_ana_logo2.png\" width=\"21\" height=\"30\"/></p></body></html>"))
        self.label_2.setText(_translate("warning", "Uyarı"))
        self.btn_close.setText(_translate("warning", "✕"))
        self.btn_tamam.setText(_translate("warning", "Tamam"))
        self.label_6.setText(_translate("warning", "HATALI GİRİŞ"))
        self.label_7.setText(_translate("warning", "⚠"))
        self.txt_error.setPlainText(_translate("warning", "Lütfen Ad Ve Soyad Alanını Boş Bırakmayınız"))

import images_rc
