import os

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

contacts = []

def load_contacts():
    if not os.path.exists("contacts.txt"):
        return

    with open("contacts.txt", "r") as in_file:
        for line in in_file:
            name, phone_number, email = line.strip().split()
            contacts.append(Contact(name, phone_number, email))

def save_contacts():
    with open("contacts.txt", "w") as out_file:
        for contact in contacts:
            out_file.write(f"{contact.name} {contact.phone_number} {contact.email}\n")

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts.append(Contact(name, phone_number, email))
    save_contacts()

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    for contact in contacts:
        print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")

    for contact in contacts:
        if contact.name == name:
            contact.phone_number = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            save_contacts()
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")

    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            save_contacts()
            return

    print("Contact not found.")

def display_menu():
    print("Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
