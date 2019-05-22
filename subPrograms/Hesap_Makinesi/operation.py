class islemler(object):
    def __init__(self):
        pass

    def toplama(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

        if self.sayi1.count(".")>0 or self.sayi2.count(".")>0:
            self.sonuc = float((float(self.sayi1) + float(self.sayi2)))
            self.virgülden_sonra = ((str(self.sonuc)).rfind(".0"))
            if self.virgülden_sonra != -1:
                self.basamak_fazlami = len((str(self.sonuc))[(self.virgülden_sonra + 2):-1:1])
                if self.basamak_fazlami > 0:
                    pass
                else:
                    self.sonuc = int(self.sonuc)

        elif self.sayi1.count(".")<1 and self.sayi2.count(".")<1:
            self.sonuc = (int(self.sayi1) + int(self.sayi2))

        if len(str(self.sonuc))>15:
            self.sonuc=round(self.sonuc,9)

        self.sonuc=str(self.sonuc)

        return self.sonuc

    def cikarma(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

        if self.sayi1.count(".") > 0 or self.sayi2.count(".") > 0:
            self.sonuc = (float(self.sayi1) - float(self.sayi2))

            self.virgülden_sonra = ((str(self.sonuc)).rfind(".0"))
            if self.virgülden_sonra != -1:
                self.basamak_fazlami = len((str(self.sonuc))[(self.virgülden_sonra + 2):-1:1])
                if self.basamak_fazlami > 0:
                    pass
                else:
                    self.sonuc = int(self.sonuc)

        elif self.sayi1.count(".") < 1 and self.sayi2.count(".") < 1:
            self.sonuc = (int(self.sayi1) - int(self.sayi2))

        if len(str(self.sonuc)) > 15:
            self.sonuc = round(self.sonuc, 9)

        self.sonuc = str(self.sonuc)
        return self.sonuc

    def carpma(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

        if self.sayi1.count(".") > 0 or self.sayi2.count(".") > 0:
            self.sonuc = (float(self.sayi1) * float(self.sayi2))

            self.virgülden_sonra = ((str(self.sonuc)).rfind(".0"))
            if self.virgülden_sonra != -1:
                self.basamak_fazlami = len((str(self.sonuc))[(self.virgülden_sonra + 2):-1:1])
                if self.basamak_fazlami > 0:
                    pass
                else:
                    self.sonuc = int(self.sonuc)

        elif self.sayi1.count(".") < 1 and self.sayi2.count(".") < 1:
            self.sonuc = (int(self.sayi1) * int(self.sayi2))

        if len(str(self.sonuc)) > 15:
            self.sonuc = round(self.sonuc, 9)

        self.sonuc = str(self.sonuc)
        return self.sonuc


    def bolme(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

        if self.sayi1.count(".") > 0 or self.sayi2.count(".") > 0:
            self.sonuc = (float(self.sayi1) / float(self.sayi2))

            self.virgülden_sonra=((str(self.sonuc)).rfind(".0"))
            if self.virgülden_sonra!=-1:
                self.basamak_fazlami=len((str(self.sonuc))[(self.virgülden_sonra+2):-1:1])
                if self.basamak_fazlami>0:
                    pass
                else:
                    self.sonuc = int(self.sonuc)

        elif self.sayi1.count(".") < 1 and self.sayi2.count(".") < 1:
            self.sonuc =int(self.sayi1)/int(self.sayi2)

        if len(str(self.sonuc)) > 5:
            self.sonuc = round(self.sonuc, 9)

        self.sonuc = str(self.sonuc)
        return self.sonuc
