'''
Password Authentication is the process of checking the identity of a user. 
Almost every online platform today makes sure that they only give access to the
real user which can be only possible by asking for a password while a user wants to
log in to the account. So in this article, 
I will take you through the task of password authentication using Python.

To create a password authentication system using Python you have to follow the steps mentioned below:

Create a dictionary of usernames with their passwords.
Then you have to ask for user input as the username by using the input function in Python.
Then you have to use the getpass module in Python to ask for user input as the password. 
Here we are using the getpass module instead of the input function to make sure that the 
user doesn’t get to see what he/she write in the password field.
'''

import getpass
database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")