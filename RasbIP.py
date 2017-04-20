import smtplib
from sys import platform
import os

def clear():
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "darwin":
            pass
        elif platform == "win32" or platform == "win64":
            os.system('cls')

def Send(To,Content):
    print("Sending...")
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("smtptestspm@gmail.com", "Testone123")
    mail.sendmail("Mail",To,Content)
    mail.close()
    clear()

def Single():
    clear()
    with open('mail.config', 'r') as f:
        mail = f.read()
    if mail == "":
        To = input("Email? ")
        with open("mail.config","w") as f:
            f.write(To)
    else:
        To = mail

    IP = os.popen("hostname -I").read()
    Content = str(IP)
    Send(To,Content)
Single()
