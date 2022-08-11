import random
import string

password = []


def update_characters_left(number_of_characters):

    global characters_left

    if number_of_characters < 0 or characters_left < number_of_characters:
        print("Nieprawidłowa liczba znaków")
        return True
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)
        return False


while True:
    password_length = int(input("Jak długie ma być hasło: "))

    if password_length < 5:
        print("Za mała liczba znaków. Hasło musi zawierać co najmniej 5 znaków")
    else:
        characters_left = password_length
        break

while True:
    lowercase_letters = int(input("Ile małych liter ma mieć hasło: "))
    result = update_characters_left(lowercase_letters)
    if not result:
        print("Małe litery: ", lowercase_letters)
        break

while True:
    uppercase_letters = int(input("Ile dużych liter ma mieć hasło: "))
    result = update_characters_left(uppercase_letters)
    if not result:
        break

while True:
    special_characters = int(input("Ile znaków specjalnych ma mieć hasło: "))
    result = update_characters_left(special_characters)
    if not result:
        break

while True:
    digits = int(input("Ile cyfr ma mieć hasło: "))
    result = update_characters_left(digits)
    if not result:
        if characters_left > 0:
            lowercase_letters += characters_left
        break

print()
print("Małe litery: ", lowercase_letters)
print("Duże litery: ", uppercase_letters)
print("Znaki specjalne: ", special_characters)
print("Liczby: ", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Wygenerowane hasło:", "".join(password))



