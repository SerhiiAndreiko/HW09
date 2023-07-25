from address_book import AddressBook, Record, Name, Phone

contacts = AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as ve:
            return str(ve)
        except IndexError:
            return "Invalid input. Please enter name and phone number separated by a space."
    return inner

def split_command(command):
    parts = command.split()
    if len(parts) < 3:
        raise ValueError("Invalid input. Please enter name and phone number separated by a space.")
    name = " ".join(parts[1:-1])
    phone = parts[-1]
    return parts[0], name, phone
@input_error
def add_contact(command):
    _, name, phone = split_command(command)
    if name in contacts.data:
        record = contacts.data[name]
    else:
        record = Record(name)
        contacts.add_record(record)

    record.add_phone(phone)
    return "Contact added successfully."


# @input_error
# def add_contact(command):
#     _, name, phone = split_command(command)
#     record = Record(name)
#     record.add_phone(phone)
#     contacts.add_record(record)
#     return "Contact added successfully."

@input_error
def change_phone(command):
    _, name, phone = split_command(command)
    if name in contacts.data:
        record = contacts.data[name]
        record.edit_phone(record.phones[0], phone)
        return "Phone number updated successfully."
    else:
        return "Contact not found."

@input_error
def get_phone(command):
    _, name = split_command(command)
    if name in contacts.data:
        record = contacts.data[name]
        return record.phones[0] if record.phones else "No phone number found."
    else:
        return "Contact not found."
    

def show_all_contacts():
    result = contacts.search_records("")
    if not result:
        return "No contacts found."
    else:
        result_str = ""
        for record in result:
            result_str += f"Name: {record.name}, Phones: {', '.join(str(p) for p in record.phones)}\n"
        return result_str

def main():
    print("How can I help you?")

    while True:
        command = input("> ").lower()

        if command == "hello":
            print("How can I help you?")

        elif command.startswith("add"):
            response = add_contact(command)
            print(response)

        elif command.startswith("change"):
            response = change_phone(command)
            print(response)

        elif command.startswith("phone"):
            response = get_phone(command)
            print(response)

        elif command == "show all":
            response = show_all_contacts()
            print(response)

        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()

