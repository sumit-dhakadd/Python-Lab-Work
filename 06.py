phonebook = {}

def add():
    person = input("Name: ")
    number = input("Phone: ")
    phonebook[person] = number
    print("Contact saved.")

def view():
    if len(phonebook) == 0:
        print("No contacts.")
    else:
        for person in phonebook:
            print(person, ":", phonebook[person])

def search():
    person = input("Search name: ")
    if person in phonebook:
        print(phonebook[person])
    else:
        print("Contact not found.")

def update():
    person = input("Update name: ")
    if person not in phonebook:
        print("Contact not found.")
    else:
        phonebook[person] = input("New phone: ")
        print("Contact updated.")

def delete():
    person = input("Delete name: ")
    if person in phonebook:
        phonebook.pop(person)
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
