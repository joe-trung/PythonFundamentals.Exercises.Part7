
def chosen_mode():
    choice = input("Please choose 1 for admin mode or 2 user mode")
    if choice == "1":
        admin_mode()
    elif choice == "2":
        multilingual_greeter
    else:
        print("invalid choice")
        chosen_mode()


def admin_mode():
    choice = input("Please choose: \n "
                   "1 to add support for additional language \n "
                   "2 to update greetings for existing languages")
    if choice == "1":
        add_language()
    elif choice == "2":
        update_greeting()
    else:
        admin_mode()


def add_language():
    language = input("Please enter new language:")
    i = len(multilingual_greeter.lang_dict) + 1
    new_language_dict = {i: language}
    multilingual_greeter.lang_dict.update(new_language_dict)




def update_greeting():
    greeting = input("Please enter greeting for new language")
    i = len(multilingual_greeter.greetings_dict) + 1
    new_greeting_dict = {i: greeting}
    multilingual_greeter.greetings_dict.update(new_greeting_dict)

chosen_mode()
print(multilingual_greeter.lang_dict)
print(multilingual_greeter.greetings_dict)
