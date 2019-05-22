# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Lenovo\Desktop\PYTHON OTOMOSYON\Todo_App\update.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setMinimumSize(QtCore.QSize(500, 500))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        Dialog.setStyleSheet("background-color: rgb(239, 255, 254);")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_detail = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_detail.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txt_detail.setFont(font)
        self.txt_detail.setStyleSheet("")
        self.txt_detail.setPlainText("")
        self.txt_detail.setObjectName("txt_detail")
        self.verticalLayout.addWidget(self.txt_detail)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(100, 40))
        self.label.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(26)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radio_tamalandi = QtWidgets.QRadioButton(Dialog)
        self.radio_tamalandi.setMinimumSize(QtCore.QSize(0, 0))
        self.radio_tamalandi.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.radio_tamalandi.setFont(font)
        self.radio_tamalandi.setIconSize(QtCore.QSize(50, 50))
        self.radio_tamalandi.setObjectName("radio_tamalandi")
        self.verticalLayout_3.addWidget(self.radio_tamalandi)
        self.radio_devam_ediyor = QtWidgets.QRadioButton(Dialog)
        self.radio_devam_ediyor.setMinimumSize(QtCore.QSize(0, 0))
        self.radio_devam_ediyor.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.radio_devam_ediyor.setFont(font)
        self.radio_devam_ediyor.setIconSize(QtCore.QSize(50, 50))
        self.radio_devam_ediyor.setObjectName("radio_devam_ediyor")
        self.verticalLayout_3.addWidget(self.radio_devam_ediyor)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.btn_guncelle = QtWidgets.QPushButton(Dialog)
        self.btn_guncelle.setMinimumSize(QtCore.QSize(100, 70))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.btn_guncelle.setFont(font)
        self.btn_guncelle.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(175, 255, 255, 255), stop:0.845771 rgba(245, 255, 255, 255));\n"
"color: rgb(45, 59, 62);\n"
"")
        self.btn_guncelle.setShortcut("")
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.horizontalLayout.addWidget(self.btn_guncelle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Güncelle"))
        self.label.setText(_translate("Dialog", "DURUM"))
        self.radio_tamalandi.setText(_translate("Dialog", "Tamamlandı"))
        self.radio_devam_ediyor.setText(_translate("Dialog", "Devam Ediyor"))
        self.btn_guncelle.setText(_translate("Dialog", "Güncelle"))

