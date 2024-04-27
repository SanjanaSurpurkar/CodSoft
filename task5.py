class Contact:
    def __init__(self, nm, ph, eml, add):
        self.nm = nm
        self.ph = ph
        self.eml = eml
        self.add = add

class ContactBook:
    def __init__(self):
        self.cont = []

    def add_cont(self, contact):
        self.cont.append(contact)
        print("Contact added successfully.")

    def view_cont(self):
        if self.cont:
            print("Contact List:")
            for contact in self.cont:
                print(f"Name: {contact.nm}, Phone: {contact.ph}")
        else:
            print("Contact list is empty.")

    def search_cont(self, search_term):
        found = False
        for contact in self.cont:
            if search_term.lower() in contact.nm.lower() or search_term in contact.ph:
                print(f"Name: {contact.nm}, Phone: {contact.ph}, Email: {contact.eml}, Address: {contact.add}")
                found = True
        if not found:
            print("No matching contact found.")

    def update_cont(self, search_term, new_contact):
        for contact in self.cont:
            if search_term.lower() in contact.nm.lower() or search_term in contact.ph:
                contact.nm = new_contact.nm
                contact.ph = new_contact.ph
                contact.eml = new_contact.eml
                contact.add = new_contact.add
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_cont(self, search_term):
        for contact in self.cont:
            if search_term.lower() in contact.nm.lower() or search_term in contact.ph:
                self.cont.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            nm = input("Enter name: ")
            ph = input("Enter phone number: ")
            eml = input("Enter email: ")
            add = input("Enter address: ")
            contact = Contact(nm, ph, eml, add)
            contact_book.add_cont(contact)

        elif ch == '2':
            contact_book.view_cont()

        elif ch == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_cont(search_term)

        elif ch == '4':
            search_term = input("Enter name or phone number of contact to update: ")
            new_nm = input("Enter new name: ")
            new_ph = input("Enter new phone number: ")
            new_eml = input("Enter new email: ")
            new_add = input("Enter new address: ")
            new_cont = Contact(new_nm, new_ph, new_eml, new_add)
            contact_book.update_cont(search_term, new_cont)

        elif ch == '5':
            search_term = input("Enter name or phone number of contact to delete: ")
            contact_book.delete_cont(search_term)

        elif ch == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
