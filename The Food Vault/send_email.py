import smtplib
from email.message import EmailMessage
import pickle
from tkinter import messagebox
import os
from project_objects import db,cur
from project_encryption_and_decryption import *
from project_invoice_creation import *



username = ''
password = ''

with open(os.getcwd() + '/csv and text files/smtp_info.txt','rb') as f:
    username = decrypt(pickle.load(f))
    password = decrypt(pickle.load(f))

smtp = smtplib.SMTP_SSL('smtp.gmail.com')
smtp.login(username,password)

def forgot_password_mail(user_name,user_email,code):
    
    msg = EmailMessage()
    msg['Subject'] = "Hey {name}, it seems that you've forgotten your passsword".format(name = user_name)
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Don't worry, we'll help you with it! </h1>
    <h3> Kindly use the following code for changing your password-</h3>
    <h4> Your verification code - {code}</h4>
    </p>
    </body>
    </html>
    """.format(code = code), subtype = 'html')

    try:
        smtp.send_message(msg)
        return True
    except ConnectionResetError:
        messagebox.showerror('Error','Connection with the server has been forcibly closed. Try restarting your system if error keeps occuring.')
        return False
    


def verification_code_mail(user_name,user_email,code):


    msg = EmailMessage()
    msg['Subject'] = "Hello {name}, We're glad to have you!".format(name = user_name)
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Welcome to our Community! </h1>
    <h3> Kindly use the following code for verifying your email-</h3>
    <h4> Your verification code - {code}</h4>
    </p>
    </body>
    </html>
    """.format(code = code), subtype = 'html')

    try:
        smtp.send_message(msg)
        return True
    except ConnectionResetError:
        messagebox.showerror('Error','Connection with the server has been forcibly closed. Try restarting your system if error keeps occuring.')
        return False
        

def email_change_alert_email(user_name,user_email,code):


    msg = EmailMessage()
    msg['Subject'] = "Email change request"
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Greetings {user_name}, </h1>
    <h3>We have received an email change request for your account</h3>
    <h4> Kindly use the following code for verifying that it's you-</h4>
    <h4> Your verification code - {code}</h4>
    </p>
    </body>
    </html>
    """.format(code = code, user_name = user_name), subtype = 'html')

    try:
        smtp.send_message(msg)
        return True
    except ConnectionResetError:
        messagebox.showerror('Error','Connection with the server has been forcibly closed. Try restarting your system if error keeps occuring.')
        return False
    

def order_placed_email(ord_id,user_name,user_email):

    file_no = 1

    while True:
        if os.path.isfile(os.getcwd() + '/Invoice/Invoice_' + str(file_no) + '.pdf') is True:
            file_no += 1
        else:
            break

    
    file_name = create_invoice(ord_id,file_no)


    msg = EmailMessage()
    msg['Subject'] = "We have received your order!"
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Your order has been placed successfully!</h1>
    <h3>Hey {user_name}! Thank you for ordering! We hope you enjoy your meal.</h3>
    <h4>Kindly find the order details in the attachements.</h4>
    </p>
    </body>
    </html>
    """.format(user_name = user_name), subtype = 'html')

    msg.add_attachment(open(file_name, "rb").read(), maintype = 'application', subtype = 'octet-stream', filename = 'Invoice.pdf')


    smtp.send_message(msg)

    os.remove(file_name)


def account_deletion_mail(user_name,user_email):

    msg = EmailMessage()
    msg['Subject'] = "Account Deletion"
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> We're sorry to know that you're leaving. </h1>
    <h3> We'll miss you {user_name}. We hope you stay safe.</h3>
    <h4>Goodbye!</h4>
    </p>
    </body>
    </html>
    """.format(user_name = user_name), subtype = 'html')


    smtp.send_message(msg)

