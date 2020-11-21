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
    if choice1 == "1":
        firstname = cleanword(
            str(input("Enter the first name of the contact: ")))
        if firstname in contactlist:
            print("First name : " + contactlist[firstname]["firstname"] + "\n" + "Last name: " + contactlist[firstname]["lastname"] +
                  "\n" + "Email: " + contactlist[firstname]["email"] + "\n" + "Phone number : " + contactlist[firstname]["number"] + "\n")
        else:
            print("No contact found!")
    elif choice1 == "2":
        contactbookopen = open("contactbook.pkl", 'wb')
        firstname = cleanword(
            str(input("Enter the first name of the contact: ")))
        lastname = cleanword(
            str(input("Enter the last name of the contact: ")))
        email = cleanword(str(input("Enter the email of the contact: ")))
        number = cleanword(str(input("Enter the number of the contact: ")))
        contactlist[firstname] = {}
        contactlist[firstname]["firstname"] = firstname
        contactlist[firstname]["lastname"] = lastname
        contactlist[firstname]["email"] = email
        contactlist[firstname]["number"] = number
        pickle.dump(contactlist, contactbookopen)
        contactbookopen.close()
        print("The contact was successfully added")
    elif choice1 == "3":
        contactbookopen = open("contactbook.pkl", 'wb')
        firstname = cleanword(
            str(input("Enter the first name of the contact: ")))
        del contactlist[firstname]
        print("The contact was successfully deleted")
    elif choice1 == "4":
        contactbookopen = open("contactbook.pkl", 'wb')
        firstname = cleanword(
            str(input("Enter the first name of the contact: ")))
        choice2 = cleanword(str(input(
            "If you want to update :\nThe contact's first name : Enter 1\nThe contact's last name : Enter 2\nThe contact's email: Enter 3\nThe contact's phone number: Enter 4")))
        choice2 = int(choice2)
        newvalue = cleanword(
            str(input("Please enter the new "+properties[choice2]+" ")))
        contactlist[firstname][properties[choice2]] = newvalue

        print("The update was successfully saved")
