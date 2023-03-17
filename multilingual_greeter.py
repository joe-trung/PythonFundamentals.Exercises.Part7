from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: "English",
    2: "Spanish",
    3: "French"
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: "What's your name?",
    2: "Como te llamas?",
    3: "Comment vous appelez-vous?"
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: "Hello",
    2: "Hola",
    3: "Bonjour"
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    print("Please choose a language: ")
    for index, language in lang_options.items():
        print(f"{index}: {language}")
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """


def language_input() -> int:
    return int(input())
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    return lang_choice in lang_options

    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    return name_prompt_options.get(lang_choice)
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """


def name_input(name_prompt: str) -> str:
    return input(name_prompt)
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    print(greetings_options.get(lang_choice) + " " + name)
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """


if __name__ == '__main__':
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
