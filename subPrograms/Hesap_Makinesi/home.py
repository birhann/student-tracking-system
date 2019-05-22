from PyQt5 import QtWidgets
from subPrograms.Hesap_Makinesi.Ui_calculator import Ui_Form
import sys
from subPrograms.Hesap_Makinesi.operation import islemler


class Pencere(Ui_Form,QtWidgets.QDialog,islemler):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.count_list=[]
        self.operator_list=[]
        self.first_count_control=None
        self.result_operate=None
        self.operation_history.setText("")
        self.two_count_control=0
        self.writing_area.setStyleSheet("")
        self.write()


    def closeEvent(self, QCloseEvent):
        self.reply= QtWidgets.QMessageBox.question(self,'Exit',
            "Çıkmak İstediğinize Emin misiniz ?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
        if self.reply==QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def write(self):
        self.one.clicked.connect(self.whileclick)
        self.two.clicked.connect(self.whileclick)
        self.three.clicked.connect(self.whileclick)
        self.four.clicked.connect(self.whileclick)
        self.five.clicked.connect(self.whileclick)
        self.six.clicked.connect(self.whileclick)
        self.seven.clicked.connect(self.whileclick)
        self.eight.clicked.connect(self.whileclick)
        self.nine.clicked.connect(self.whileclick)
        self.zero.clicked.connect(self.whileclick)
        self.clear_line.clicked.connect(self.whileclick)
        self.clear_all.clicked.connect(self.clear)
        self.back.clicked.connect(self.whileclick)


        self.virgul.clicked.connect(self.whileclick)
        self.arti_eksi.clicked.connect(self.whileclick)

        self.toplama.clicked.connect(self.operation)
        self.cikarma.clicked.connect(self.operation)
        self.carpma.clicked.connect(self.operation)
        self.bolme.clicked.connect(self.operation)

        self.esittir.clicked.connect(self.whileclick)

    def count_capaticy(self):
        if self.writing_area.styleSheet() == "":
            if len(str(self.writing_area.toPlainText())) > 10:
                self.writing_area.setStyleSheet("font: 30pt 'MS Shell Dlg 2';")
                print("font30")
                return True

        if self.writing_area.styleSheet() == "font: 30pt 'MS Shell Dlg 2';":
            if len(str(self.writing_area.toPlainText())) > 13:
                self.writing_area.setStyleSheet("font: 25pt 'MS Shell Dlg 2';")
                print("font25")
                return True

        if self.writing_area.styleSheet() == "font: 25pt 'MS Shell Dlg 2';":
            if len(str(self.writing_area.toPlainText())) > 15:
                self.writing_area.setStyleSheet("font: 20pt 'MS Shell Dlg 2';")
                print("font20")
                return True

        if self.writing_area.styleSheet() == "font: 20pt 'MS Shell Dlg 2';":
            if len(str(self.writing_area.toPlainText())) > 19:
                print("False")
                return False
    def change_last_operation(self):
        self.data_operation = self.veri1

        self.data_operation1 = self.data_operation.replace("x", "one")
        self.data_operation1 = self.data_operation1.replace("/", "one")
        self.data_operation1 = self.data_operation1.replace("+", "one")

        if (self.data_operation1).count("-") > 1:
            self.a = self.writing_area.toPlainText()
            self.b = self.data_operation1
            self.b = (((self.b).replace("(" + self.a + ")", "~")).replace("-", "one")).replace("~", "(" + self.a + ")")
            self.data_operation1 = self.b
        else:
            self.data_operation1 = self.data_operation1.replace("-", "one")

        return self.data_operation1

    def mat_islemi1(self):
        self.sayi_uzunlugu=self.sayi_uzunlugu1
        self.islem_gecmisi=(self.operation_history.text()).replace("(","")
        self.islem_gecmisi=(self.operation_history.text()).replace(")","")

        self.aralik=len(self.islem_gecmisi)-(self.sayi_uzunlugu)
        self.count_for_math=(self.islem_gecmisi)[self.aralik:-1:1]
        self.count_for_math=(self.count_for_math).replace(" ","")


        self.count_for_math_count=(self.count_for_math)[0:((len(self.count_for_math))-1):1]
        self.operator_for_mat=(self.count_for_math)[-1]
    def mat_islemi(self):
        self.mat_islemi1()

        if (self.two_count_control) > 1:
            self.operator = self.operator_for_mat
            self.count = self.count_for_math_count
            self.count_list.append(self.count)
            self.operator_list.append(self.operator)
            self.first_control=list(zip((self.count_list),(self.operator_list)))
            result = self.math_result()
            return result

        else:
            self.operator = self.operator_for_mat
            self.count = self.count_for_math_count
            self.count_list.append(self.count)
            self.operator_list.append((self.operator))
            return self.count_list[0]

    def math_result(self):
        if self.first_count_control==None:
            self.first_count =((self.first_control)[-2][0])
            self.first_count_control="All Right Reserved"


        self.first_operator = str((self.first_control)[-2][1])
        self.second_count = str((self.first_control)[-1][0])

        if self.first_operator == "+":
            self.result = islemler.toplama(self, self.first_count, self.second_count)
            self.first_count = self.result
            return self.first_count

        elif self.first_operator == "-":
            self.result = islemler.cikarma(self, self.first_count, self.second_count)
            self.first_count = self.result
            return self.first_count
        elif self.first_operator == "x":
            self.result = islemler.carpma(self, self.first_count, self.second_count)
            self.first_count = self.result
            return self.first_count
        elif self.first_operator == "/":
            self.result = islemler.bolme(self, self.first_count, self.second_count)
            self.first_count = self.result
            return self.first_count

    def operation(self):
        sender=self.sender()
        if sender.text() == "+":
            if self.result_operate==self.writing_area.toPlainText():
                # changing operator
                self.data = self.change_last_operation()
                self.data = self.data.replace("one", "+")

                self.ope_hist_end = len(self.operation_history.text()) - len(self.veri1)
                self.operation_history.setText((self.operation_history.text()[0:self.ope_hist_end:1]) + self.data)
                self.veri1 = self.data
                self.operator_list.pop()
                self.operator_list.append("+")
            else:
                try:
                    self.veri = self.writing_area.toPlainText()

                    # settext operation history
                    if self.veri[-1] == ".":
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(self.operation_history.text() + "(" + (self.veri).strip(".") + ") + ")
                            self.veri1="(" + (self.veri).strip(".") + ") + "

                        else:
                            self.operation_history.setText(self.operation_history.text() + (self.veri).strip(".") + " + ")
                            self.veri1= (self.veri).strip(".") + " + "
                    else:
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(self.operation_history.text() + "(" + self.veri + ") + ")
                            self.veri1="(" + self.veri + ") + "
                        else:
                            self.operation_history.setText(self.operation_history.text() + self.veri + " + ")
                            self.veri1=self.veri + " + "

                    #checking length of operation history
                    if len(self.operation_history.text())>40:
                        self.operation_history.clear()
                        self.operation_history.setText(self.veri1)

                    self.two_count_control += 1
                    self.sayi_uzunlugu1 = 3 + (len((self.writing_area.toPlainText()).strip(".")))

                    # resetting size of writing area
                    self.writing_area.setStyleSheet("")

                    # checking length of writing area
                    self.result_operate = str(self.mat_islemi())
                    if len(self.result_operate) > 11:
                        self.writing_area.setStyleSheet("font: 30pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 14:
                        self.writing_area.setStyleSheet("font: 25pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 16:
                        self.writing_area.setStyleSheet("font: 20pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 20:
                        self.result_operate = round((float(self.result_operate)), 20)

                    self.result_operate = str(self.result_operate)
                    self.writing_area.clear()
                    self.writing_area.insertPlainText((self.result_operate))
                    self.toplama.setStyleSheet("background-color:None")
                except:
                    self.toplama.setStyleSheet("QPushButton:pressed { background-color: #ffabab }")

        elif sender.text() == "-":
            if self.result_operate==self.writing_area.toPlainText():
                # changing operator
                self.data = self.change_last_operation()
                self.data = self.data.replace("one", "-")

                self.ope_hist_end = len(self.operation_history.text()) - len(self.veri1)
                self.operation_history.setText((self.operation_history.text()[0:self.ope_hist_end:1]) + self.data)
                self.veri1 = self.data
                self.operator_list.pop()
                self.operator_list.append("-")
            else:
                try:
                    self.veri = self.writing_area.toPlainText()
                    # settext operation history
                    if self.veri[-1] == ".":
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(self.operation_history.text() + "(" + (self.veri).strip(".") + ") - ")
                            self.veri1="(" + (self.veri).strip(".") + ") - "
                        else:
                            self.operation_history.setText(self.operation_history.text() + (self.veri).strip(".") + " - ")
                            self.veri1 = (self.veri).strip(".") + " - "
                    else:
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(self.operation_history.text() + "(" + self.veri + ") - ")
                            self.veri1="(" + self.veri + ") - "
                        else:
                            self.operation_history.setText(self.operation_history.text() + self.veri + " - ")
                            self.veri1=self.veri + " - "

                    # checking length of operation history
                    if len(self.operation_history.text()) > 40:
                        self.operation_history.clear()
                        self.operation_history.setText(self.veri1)

                    self.two_count_control += 1
                    self.sayi_uzunlugu1 = 3 + (len((self.writing_area.toPlainText()).strip(".")))

                    # resetting size of writing area
                    self.writing_area.setStyleSheet("")

                    # checking length of writing area
                    self.result_operate = str(self.mat_islemi())
                    if len(self.result_operate) > 11:
                        self.writing_area.setStyleSheet("font: 30pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 14:
                        self.writing_area.setStyleSheet("font: 25pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 16:
                        self.writing_area.setStyleSheet("font: 20pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 20:
                        self.result_operate = round((float(self.result_operate)),20)

                    self.result_operate = str(self.result_operate)
                    self.writing_area.clear()
                    self.writing_area.insertPlainText(self.result_operate)
                    self.cikarma.setStyleSheet("background-color:None")
                except:
                    self.cikarma.setStyleSheet("QPushButton:pressed { background-color: #ffabab }")

        elif sender.text()=="x":
            if self.result_operate==self.writing_area.toPlainText():
                # changing operator
                self.data = self.change_last_operation()
                self.data = self.data.replace("one", "x")

                self.ope_hist_end = len(self.operation_history.text()) - len(self.veri1)
                self.operation_history.setText((self.operation_history.text()[0:self.ope_hist_end:1]) + self.data)
                self.veri1 = self.data
                self.operator_list.pop()
                self.operator_list.append("x")
            else:
                try:
                    self.veri = self.writing_area.toPlainText()
                    # settext operation history
                    if self.veri[-1] == ".":
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(
                                self.operation_history.text() + "(" + (self.veri).strip(".") + ") x ")
                            self.veri1="(" + (self.veri).strip(".") + ") x "
                        else:
                            self.operation_history.setText(self.operation_history.text() + (self.veri).strip(".") + " x ")
                            self.veri1 =(self.veri).strip(".") + " x "
                    else:
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(self.operation_history.text() + "(" + self.veri + ") x ")
                            self.veri1="(" + self.veri + ") x "
                        else:
                            self.operation_history.setText(self.operation_history.text() + self.veri + " x ")
                            self.veri1=self.veri + " x "

                    # checking length of operation history
                    if len(self.operation_history.text()) > 40:
                        self.operation_history.clear()
                        self.operation_history.setText(self.veri1)

                    self.two_count_control += 1
                    self.sayi_uzunlugu1 = 3 + (len((self.writing_area.toPlainText()).strip(".")))

                    # resetting size of writing area
                    self.writing_area.setStyleSheet("")

                    # checking length of writing area
                    self.result_operate = str(self.mat_islemi())
                    if len(self.result_operate) > 11:
                        self.writing_area.setStyleSheet("font: 30pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 14:
                        self.writing_area.setStyleSheet("font: 25pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 16:
                        self.writing_area.setStyleSheet("font: 20pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 20:
                        self.result_operate=round((float(self.result_operate)),20)

                    self.result_operate=str(self.result_operate)
                    self.writing_area.clear()
                    self.writing_area.insertPlainText(self.result_operate)
                    self.carpma.setStyleSheet("background-color:None")

                except:
                    self.carpma.setStyleSheet("QPushButton:pressed { background-color: #ffabab }")

        elif sender.text()=="÷":
            if self.result_operate==self.writing_area.toPlainText():
                # changing operator
                self.data = self.change_last_operation()
                self.data = self.data.replace("one", "/")

                self.ope_hist_end = len(self.operation_history.text()) - len(self.veri1)
                self.operation_history.setText((self.operation_history.text()[0:self.ope_hist_end:1]) + self.data)
                self.veri1 = self.data
                self.operator_list.pop()
                self.operator_list.append("/")

            else:
                try:
                    self.veri = self.writing_area.toPlainText()


                    # settext operation history
                    if self.veri[-1] == ".":
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(
                                self.operation_history.text() + "(" + (self.veri).strip(".") + ") / ")
                            self.veri1="(" + (self.veri).strip(".") + ") / "
                        else:
                            self.operation_history.setText(self.operation_history.text() + (self.veri).strip(".") + " / ")
                            self.veri1 =(self.veri).strip(".") + " / "
                    else:
                        if self.veri.count("-") > 0:
                            self.operation_history.setText(self.operation_history.text() + "(" + self.veri + ") / ")
                            self.veri1 ="(" + self.veri + ") / "
                        else:
                            self.operation_history.setText(self.operation_history.text() + self.veri + " / ")
                            self.veri1 =self.veri + " / "

                    # checking length of operation history
                    if len(self.operation_history.text()) > 40:
                        self.operation_history.clear()
                        self.operation_history.setText(self.veri1)

                    self.two_count_control += 1
                    self.sayi_uzunlugu1 = 3 + (len((self.writing_area.toPlainText()).strip(".")))

                    # resetting size of writing area
                    self.writing_area.setStyleSheet("")
                    #checking length of writing area
                    self.result_operate = str(self.mat_islemi())
                    if len(self.result_operate) > 11:
                        self.writing_area.setStyleSheet("font: 30pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 14:
                        self.writing_area.setStyleSheet("font: 25pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 16:
                        self.writing_area.setStyleSheet("font: 20pt 'MS Shell Dlg 2';")
                    if len(self.result_operate) > 20:
                        self.result_operate=round((float(self.result_operate)),20)

                    self.result_operate = str(self.result_operate)
                    self.writing_area.clear()
                    self.writing_area.insertPlainText(self.result_operate)
                    self.bolme.setStyleSheet("background-color:None")

                except:
                    self.bolme.setStyleSheet("QPushButton:pressed { background-color: #ffabab }")

    def clear2(self):
        self.writing_area.clear()
        self.operation_history.clear()
        self.two_count_control = 0
        self.first_count_control = None
        self.operator_list.clear()
        self.count_list.clear()
        self.writing_area.setStyleSheet("font: None")
        self.writing_area.setStyleSheet("")

    def equal_settings(self):
        if len(self.operator_list) == 1:
            if self.operator_list[-1] == "+":
                self.islem = islemler.toplama(self,(self.count_list[-1]),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem
            if self.operator_list[-1] == "-":
                self.islem = islemler.cikarma(self,(self.count_list[-1]),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem
            if self.operator_list[-1] == "x":
                self.islem = islemler.carpma(self,(self.count_list[-1]),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem
            elif self.operator_list[-1] == "/":
                self.islem = islemler.bolme(self,(self.count_list[-1]),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem

        elif len(self.operator_list)>1:
            if self.operator_list[-1] == "+":
                self.islem = islemler.toplama(self,(self.result_operate),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem
            elif self.operator_list[-1] == "-":
                self.islem =islemler.cikarma(self,(self.result_operate),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem
            elif self.operator_list[-1] == "x":
                self.islem = islemler.carpma(self,(self.result_operate),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem
            elif self.operator_list[-1] == "/":
                self.islem =islemler.bolme(self,(self.result_operate),(self.writing_area.toPlainText()))
                self.clear2()
                return self.islem




    def whileclick(self):
        sender=self.sender()
        if sender.text()=="=":
            if len(self.operator_list)==1:
                self.writing_area.insertPlainText(self.equal_settings())
                self.result_operate=self.writing_area.toPlainText()
            elif len(self.operator_list)>1:
                if self.writing_area.toPlainText()!=self.result_operate:
                    self.writing_area.insertPlainText(self.equal_settings())
                    self.result_operate = self.writing_area.toPlainText()



        elif sender.text()=="1":
            self.count_adding_control= self.count_capaticy()
            if self.count_adding_control==False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("1")
                else:
                    pass
            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("1")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("1")
                    else:
                        self.writing_area.insertPlainText("1")
                except:
                    self.writing_area.insertPlainText("1")

        elif sender.text()=="2":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("2")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("2")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("2")
                    else:
                        self.writing_area.insertPlainText("2")
                except:
                    self.writing_area.insertPlainText("2")



        elif sender.text()=="3":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("3")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("3")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("3")
                    else:
                        self.writing_area.insertPlainText("3")
                except:
                    self.writing_area.insertPlainText("3")
        elif sender.text()=="4":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("4")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("4")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("4")
                    else:
                        self.writing_area.insertPlainText("4")
                except:
                    self.writing_area.insertPlainText("4")
        elif sender.text()=="5":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("5")
                else:
                    pass
            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("5")

                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("5")
                    else:
                        self.writing_area.insertPlainText("5")
                except:
                    self.writing_area.insertPlainText("5")
        elif sender.text()=="6":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("6")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("6")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("6")
                    else:
                        self.writing_area.insertPlainText("6")
                except:
                    self.writing_area.insertPlainText("6")
        elif sender.text()=="7":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("7")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("7")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("7")
                    else:
                        self.writing_area.insertPlainText("7")
                except:
                    self.writing_area.insertPlainText("7")
        elif sender.text()=="8":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("8")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("8")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("8")
                    else:
                        self.writing_area.insertPlainText("8")
                except:
                    self.writing_area.insertPlainText("8")
        elif sender.text()=="9":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("9")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("9")

                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("9")

                    else:
                        self.writing_area.insertPlainText("9")
                except:
                    self.writing_area.insertPlainText("9")
        elif sender.text()=="0":
            self.count_adding_control = self.count_capaticy()
            if self.count_adding_control == False:
                if self.result_operate == str(self.writing_area.toPlainText()):
                    self.writing_area.clear()
                    self.writing_area.setStyleSheet("")
                    self.writing_area.insertPlainText("0")
                else:
                    pass

            else:
                try:
                    if self.result_operate==str(self.writing_area.toPlainText()):
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("0")
                    elif self.writing_area.toPlainText()=="0":
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("0")
                    else:
                        self.writing_area.insertPlainText("0")
                except:
                    self.writing_area.insertPlainText("0")

        elif sender.text()=="CE":
            self.writing_area.clear()
            self.writing_area.insertPlainText("0")


        elif sender.text()==".":
            try:
                tip=type(int(self.writing_area.toPlainText()))
                if self.writing_area.toPlainText().count(".")>0:
                    self.virgul.setStyleSheet("QPushButton:pressed { background-color: red }")

                else:
                    if str(self.result_operate)==self.writing_area.toPlainText():
                        self.writing_area.clear()
                        self.writing_area.insertPlainText("0.")
                    else:
                        self.writing_area.insertPlainText(".")

                    self.virgul.setStyleSheet("background-color: None;")
            except:
                self.virgul.setStyleSheet("QPushButton:pressed { background-color: #ffabab }")

        elif sender.text()=="↵":

            if self.writing_area.toPlainText()==self.result_operate:
                self.back.setStyleSheet("QPushButton:pressed { background-color: #ffabab }")
            else:
                veri=self.writing_area.toPlainText()
                liste=[]
                for i in veri:
                    liste.append(i)
                counts=""
                for i in range(0,(len(veri))-1):
                    counts+=liste[i]
                self.writing_area.clear()
                self.writing_area.insertPlainText(counts)

        elif sender.text()=="+-":
            self.rakam=self.writing_area.toPlainText()
            if self.rakam.count("-")>0:
                self.rakam=self.rakam.strip("-")
                self.writing_area.clear()
                self.writing_area.insertPlainText(self.rakam)
            elif self.writing_area.toPlainText()=="0":
                pass
            else:
                self.writing_area.clear()
                self.writing_area.insertPlainText("-"+self.rakam)

    def clear(self):
        self.writing_area.clear()
        self.operation_history.clear()
        self.two_count_control = 0
        self.first_count_control = None
        self.result_operate = None
        self.operator_list.clear()
        self.count_list.clear()
        self.writing_area.setStyleSheet("font: None")
        self.writing_area.setStyleSheet("")
        self.writing_area.insertPlainText("0")







if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=Pencere()
    window.show()
    sys.exit(app.exec_())
