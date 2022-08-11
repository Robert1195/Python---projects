import json
import random
import sys

points = 0
questions_list = []
category = None


def show_questions(questions):
    global points

    print()
    print(questions["pytanie"])
    print("a:", questions["a"])
    print("b:", questions["b"])
    print("c:", questions["c"])
    print("d:", questions["d"])
    print()

    while True:
        answer = input("Którą odpowiedź wybierasz ?")
        if answer == questions["prawidłowa_odpowiedź"]:
            points += 1
            print("Brawo, prawidłowa odpowiedź. " + "Zdobyłeś " + str(points) + " punkty.")
            break
        elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Błędna wartość, podaj a, b, c lub d")
        else:
            print("Błędna odpowiedź, masz", points, "punkty")
            print("Poprawna odpowiedź to: " + questions["prawidłowa_odpowiedź"])
            break


def choice_category(user_choice):
    global category
    if user_choice == "1":
        category = "nauka"
    elif user_choice == "2":
        category = "technologia"
    elif user_choice == "3":
        category = "film"
    else:
        print("Niepoprada wartość, wybierz kategorię 1, 2 lub 3")
    return category


while True:

    while True:

        isContinue = True
        questions_list.clear()
        counter = 0

        print("QUIZ")
        print()
        print("1 - nauka")
        print("2 - technologia")
        print("3 - film")

        user_choice = input("Wybierz kategorię ")
        category = choice_category(user_choice)
        if category == "nauka" or category == "technologia" or category == "film":  # warunek na wyjście z pętli jeśli wybrór jest poprawny
            break

    with open("main.json", encoding="UTF-8") as json_file:
        questions = json.load(json_file)

        for i in questions:
            if i["kategoria"] == category:
                counter += 1

        for i in range(0, len(questions)):

            while isContinue:

                question = random.choice(questions)

                if question not in questions_list and question["kategoria"] == category:
                    questions_list.append(question)
                    show_questions(question)
                elif len(questions_list) == counter:
                    print("Koniec pytań z wybranej kategorii")
                    while True:
                        is_continue = input("Czy chcesz zagrać jeszcze raz, Y/N ? ").upper()
                        if is_continue == "Y":
                            isContinue = False
                            break
                        elif is_continue == "N":
                            sys.exit(0)
                        else:
                            print("Niewłaściwy wybór, wybierz Y lub N")

