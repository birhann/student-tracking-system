import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sendMail(object):
    def __init__(self,mail_adress,subject,body):
        print("Trying..")
        mail = MIMEMultipart()
        mail['From'] = "{}".format("ogrencitakipsistemi@outlook.com")
        mail['Subject'] = "{}".format(subject)
        mail.attach(MIMEText(body, "html"))

        for adress in mail_adress:

            if adress.count("outlook.com")>0:
                server = smtplib.SMTP("smtp.office365.com", 587)
                mail['To']=adress

            elif adress.count("gmail.com")>0:
                server=smtplib.SMTP("smtp.gmail.com",587)
                mail['To'] = adress

            elif adress.count("icloud.com")>0:
                server=smtplib.SMTP("smtp.mail.me.com",587)
                mail['To'] = adress

            elif adress.count("hotmail.com")>0:
                server = smtplib.SMTP("smtp.office365.com", 587)
                mail['To'] = adress
            else:
                continue
            try:
                server.starttls()
                print(mail['To'])
                server.login(mail['From'], '775477ogrencitakip')
                server.sendmail(mail['From'], mail['To'], mail.as_string())
                server.quit()
                print("Gönderildi")
            except:
                print("Mail Gönderilemedi")

