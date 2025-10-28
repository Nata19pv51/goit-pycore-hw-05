def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"The name was not found."
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "You are trying to access an item that does not exist!"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts.update({name: phone})
    return "Contact updated."
        
    # if name in contacts:
    #     contacts.update({name: phone})
    #     return "Contact updated."
    # else:
    #     return "There is not this contact."
        
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
    # return contacts.get(name)

    # if name in contacts:
    #     return contacts.get(name)
    # else:
    #     return "There is not this contact."

def show_all(contacts):
    result = ""
    
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    
    if len(result) == 0:
        result = "No contacts"
    else:
        result = result[:- 1]
    
    return result
        
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
