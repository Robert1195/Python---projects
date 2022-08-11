import sys
import random


# funkcja zwraca indeks litery podanej przez użytkownika
def find_indexes(word, user_letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter_in_word == user_letter:
            indexes.append(index)
    return indexes


# funkcja wyświetla status gry
def show_results():
    print("Szukane słowo {}".format(user_word))
    print("Pozostało prób: {}".format(number_of_tries))
    print("Użyłeś następującuch liter:{}".format(used_letters))
    print()


# wybór poziomu trudności
def choice_difficulty_level(difficulty_level):
    number_of_tries = None

    if difficulty_level == "1":
        number_of_tries = 10
    elif difficulty_level == "2":
        number_of_tries = 8
    elif difficulty_level == "3":
        number_of_tries = 6
    else:
        print("Niepoprada wartość, wybierz liczbę 1, 2 lub 3")
    return number_of_tries


words_to_guess = []

# pobranie haseł z pliku i zapisanie do listy
with open("hasla.txt", "r") as file:
    for w in file:
        words_to_guess.append(w.split("\n")[0])

while True:

    word = random.choice(words_to_guess)
    words_to_guess.remove(word)

    used_letters = []
    user_word = []

    for _ in word:  # dodanie znaku "-" zamiast liter w haśle
        user_word.append("-")

    print("GRA - ZGADNIJ HASŁO")
    print()
    print("1 - łatwy")
    print("2 - normalny")
    print("3 - trudny")

    while True:
        difficulty_level = input("Wybierz poziom trudności: ")
        number_of_tries = choice_difficulty_level(difficulty_level)
        if type(number_of_tries) == int:  # warunek na wyjście z pętli jeśli wybrór jest poprawny
            break

    is_continue = True

    while is_continue:

        user_letter = input("Podaj literę: ")

        if not user_letter.isalpha():  # walidacja znaku podanego przez użytkownika
            print("Podany znak musi być literą")
        elif len(user_letter) != 1:
            print("Podaj tylko jedną literę")
            print()
        elif user_letter in used_letters:
            print("Litera została już użyta, podaj inna literę")
        else:
            used_letters.append(user_letter)
            found_indexes = find_indexes(word, user_letter)
            if len(found_indexes) == 0:  # sprawdzenie czy litera jest poprawna, czy lista z indeksami nie jest pusta
                number_of_tries -= 1
                print("Nie ma takiej litery")
                if number_of_tries == 0:
                    print("Koniec gry, straciłeś wszystkie życia")
                    while True:
                        user_choice = input("Czy chcesz zagrać jeszcze raz ?: Y/N:".upper())  # reset gry
                        if user_choice.upper() == "Y":  # walidacja wartości wpisanej przez użytkownika
                            is_continue = False
                            break
                        elif user_choice.upper() == "N":
                            sys.exit(0)
                        else:
                            print("Błędny wybór, wybierz Y lub N")
            else:
                print("Poprawna litera")
                for index in found_indexes:
                    user_word[index] = user_letter  # podmiana _ na znalezioną literę

                if "".join(user_word) == word:  # sprawdzenie czy wszystkie litery zostały znalezione
                    print("Gratulacje, wygrałeś!")
                    if len(words_to_guess) == 0:  # sprawdzenie czy wszystkie hasło zostały zgadnięte
                        print("Koniec gry, zgadłeś wszystkie hasła !")
                        sys.exit(0)
                    while True:
                        user_choice = input("Czy chcesz zagrać jeszcze raz ?: Y/N")  # reset gry
                        if user_choice.upper() == "Y":
                            is_continue = False
                            break
                        elif user_choice.upper() == "N":
                            sys.exit(0)
                        else:
                            print("Błędny wybór, wybierz Y lub N")


        show_results()
