class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
    else:
        for contact in contacts:
            print(contact)

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            print(contact)
            found = True
    if not found:
        print("No contact found.\n")

def delete_contact(contacts):
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("No contact found to delete.\n")

def main():
    contacts = []
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
