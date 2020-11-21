import pickle
import os

filesize = os.path.getsize("contactbook.pkl")
contactbookread = open("contactbook.pkl", 'rb')

if filesize == 0:
    contactlist = {}
else:
    contactlist = pickle.load(contactbookread)


def cleanword(n):
    n = n.lower()
    n = n.strip()
    return(n)
