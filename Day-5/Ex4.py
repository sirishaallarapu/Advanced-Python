def display_menu():
    print("\nContact List Management")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if contacts:
        print("\nYour Contacts List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Your contact list is empty.")

def update_contact(contacts):
    if contacts:
        phone = input("Enter the phone number of the contact you want to update: ")
        contact_found = False
        for contact in contacts:
            if contact["phone"] == phone:
                contact_found = True
                name = input("Enter new contact name: ")
                phone = input("Enter new contact phone number: ")
                email = input("Enter new contact email: ")
                contact.update({"name": name, "phone": phone, "email": email})
                print(f"Contact updated successfully.")
                break
        if not contact_found:
            print("Contact with the given phone number not found.")
    else:
        print("Your contact list is empty.")

def delete_contact(contacts):
    if contacts:
        phone = input("Enter the phone number of the contact you want to delete: ")
        contact_found = False
        for contact in contacts:
            if contact["phone"] == phone:
                contact_found = True
                contacts.remove(contact)
                print(f"Contact with phone number '{phone}' deleted successfully.")
                break
        if not contact_found:
            print("Contact with the given phone number not found.")
    else:
        print("Your contact list is empty.")

def main():
    contacts = []

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-5): "))
            
            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                view_contacts(contacts)
            elif choice == 3:
                update_contact(contacts)
            elif choice == 4:
                delete_contact(contacts)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option (1-5).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

