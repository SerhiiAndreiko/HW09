contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter name and phone number separated by a space."
    return inner

def split_command(command):
    return command.split()

@input_error
def add_contact(command):
    _, name, phone = split_command(command)
    contacts[name] = phone
    return "Contact added successfully."

@input_error
def change_phone(command):
    _, name, phone = split_command(command)
    contacts[name] = phone
    return "Phone number updated successfully."

@input_error
def get_phone(command):
    _, name = split_command(command)
    return contacts[name]

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"Name: {name}, Phone: {phone}\n"
        return result

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

