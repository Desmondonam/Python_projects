'''
This code will be hte one that gives a guide to how you can send automatic emails
'''

import os
import random
import smtplib


def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, Welcome to Desney Company")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("desmondonam@gmail.com", "You_App+Password")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()