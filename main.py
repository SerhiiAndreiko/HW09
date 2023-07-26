import address_book as ab
from functools import wraps

def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ",1)
            args = (s.strip() for s in args)
            return command, args
    return command_line.lower(),()


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Sorry, there are not enough parameters or their value may be incorrect. "\
                   "Please use the help for more information."
        except Exception as e:
            return "**** Exception other" + e
    return wrapper    


@input_error
def command_add(*args) -> str:
    user = args[0]
    args[1]
    phone = [ ab.Phone(p) for p in args[1:] ]
    if user in a_book:
        a_book.get_record(user).add_phone(phone)
    else:
        rec = ab.Record(ab.Name(user), phone)
        a_book.add_record(rec)
    return "Done"



@input_error
def command_change_phone(*args) -> str:
    user = args[0]
    old_phone = args[1]
    new_phone = args[2]
    a_book.get_record(user).change_phone(ab.Phone(old_phone), ab.Phone(new_phone))
    return "Done"


@input_error
def command_show_phone(*args) -> str:
    user = args[0]
    return a_book.get_record(user).get_phones()


def command_show_all(*args) -> str:
    if any(a_book.keys()):
        return a_book
    else:
        return "No users found, you must first add name and phone"


def greetings(*args) -> str:
    return "Hello! How can I help you?"

@input_error
def command_delete_record(*args) -> str:
    user = args[0]
    a_book.remove_record(user)
    return "Done"

@input_error
def command_delete_phone(*args) -> str:
    user = args[0]
    phone = args[1]
    a_book.get_record(user).remove_phone(ab.Phone(phone))
    return "Done" 

def command_help(*args) -> str:
    command = " ".join(args)
    if not command:
        commands = list(COMMANDS.keys())
        commands.extend(COMMAND_EXIT)
        return "List of commands: " + ", ".join(commands)
    else:
        return COMMANDS_HELP.get(command,  f"Help for this command '{command}' is not yet available")


COMMAND_EXIT=("good bye", "close", "exit")

COMMANDS = {
    "hello": greetings,
    "add": command_add,
    "change": command_change_phone,
    "phone": command_show_phone ,
    "show all": command_show_all,
    "help": command_help,
    "delet record": command_delete_record,
    "delet phone": command_delete_phone
}

COMMANDS_HELP = {
    "hello": "Say hello",
    "add": "Add user and phone. Required username and phone.",
    "change": "Change user's phone. Required username and phone.",
    "phone": "Show user's phone. Required username." ,
    "delet record": "Delet record of user ",
    "delet phone": "Delet phone record of user",
    "show all": "Show all user phone numbers.",
    "help": "List of commands  and their description.",
    "exit": "Exit of bot.",
    "close": "Exit of bot." ,
    "good bye": "Exit of bot."
}

a_book = ab.AddressBook()

def main():
    print("Welcome to the Address Book CLI")
    while True:
        try:
            user_input = input("Enter your command:")
        except KeyboardInterrupt:
            print("\r")
            break
        if user_input.lower() in COMMAND_EXIT:
            break
        else:
            command, args = parse_input(user_input)
            try:
                result=COMMANDS[command](*args)
            except KeyError:
                 print("Your command is not recognized, try to enter other command. "
                       "To get a list of all commands, you can use the 'help' command")
            else:
                if result:
                    print(result)
    print("Good bye")

if __name__ == "__main__":
    main()

