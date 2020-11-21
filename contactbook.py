import pickle
import os

filesize = os.path.getsize("contactbook.pkl")
contactbookread = open("contactbook.pkl", 'rb')
properties = [0, "firstname", "lastname", "email", "number"]

if filesize == 0:
    contactlist = {}
else:
    contactlist = pickle.load(contactbookread)


def cleanword(n):
    n = n.lower()
    n = n.strip()
    return(n)


print("Hello!")


def function():
    choice1 = (str(input(
        "If you want to :\nShow contact: Enter 1\nAdd a contact: Enter 2\nRemove a contact: Enter 3\nUpdate a contact: Enter 4\nShow a summary of all contacts: Enter 5\nClose the contact book app: Press x :\n")))
