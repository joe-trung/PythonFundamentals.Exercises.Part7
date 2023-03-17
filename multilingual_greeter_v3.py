import random
import multilingual_greeter


greetings_new_dict = {
    1: ["Hello", "Hi", "Hey"],
    2: ["Hola", "Oye!", "Que onda"],
    3: ["Bonjour", "Salut", "Coucou"]
}

def random_greeter():
    print(multilingual_greeter.lang_dict)
    key_input = int(input("Please select a language to greet, enter number:"))
    rand_greeting = random.choice(greetings_new_dict[key_input])
    print(rand_greeting + " Name")

random_greeter()
