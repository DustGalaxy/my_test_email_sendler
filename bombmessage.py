# -*- coding: utf-8 -*-
import smtplib
import json
from validate_email import validate_email
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BombMessage():
    '''
    Сlass to implement the email bombs funcionality
    filename: str           - path to the message file
    my_address: str         - address from which the message will send
    password: str           - app password from google account
    addresses: list         - email addresses to which the message
                              will sent
    subject: str            - email sibject, can be changed later

    def send_bomb(self):    - Send a message

    def edit_subject(self): - Proposes to change the subject
    def add_address(self):  - Adds a new address
    def del_address(self):  - Deletes a address
    def _save(self):        - Save changes to the json file
    '''
    filename: str

    sendler: str
    __password: str
    addresses: list

    subject: str
    msg: MIMEMultipart
    content: MIMEText

    def __init__(self, filename, my_address, password, addresses, subject):
        self.filename = filename

        self.sendler = my_address
        self.__password = password
        self.addresses = addresses

        self.msg = MIMEMultipart()
        with open(self.filename, 'r', encoding='utf-8') as fp:
            self.content = MIMEText(fp.read())
            print(self.content.as_string)
        self.subject = subject

    def send_bomb(self):
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.sendler
        self.msg['To'] = ', '.join(self.addresses)
        self.msg.attach(self.content)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.sendler, self.__password)
            server.sendmail(self.sendler, self.addresses, self.msg.as_string())
            print("Message sent.")

    def edit_subject(self):
        try:
            self.msg['Subject'] = self.subject = str(input("Input new subject >> "))
        except Exception as e:
            print(f"{e}")

    def add_address(self):
        try:
            address = str(input("Input address >> "))
            if validate_email(address):
                self.addresses.append(address)
                self.msg["To"] = ', '.join(self.addresses)
                self._save()
            else:
                raise ValueError
        except Exception as e:
            print("Invalid input address", e)

    def del_address(self):
        try:
            to_remove = str(input('Input address to delete >> '))
            self.addresses.remove(to_remove)
            self.msg["To"] = ', '.join(self.addresses)
            self._save()
        except Exception as e:
            print("Invalid input address", e)

    def _save(self):
        data = {
            "filename": self.filename,
            "to": self.addresses,
            "from": self.sendler,
            "password": self.__password,
            "subject": self.msg['Subject']
        }

        try:
            with open("config.json", 'w') as file:
                json.dump(data, file, indent=4)
                print("Save is complete")
        except Exception as e:
            print(f"{e}")
