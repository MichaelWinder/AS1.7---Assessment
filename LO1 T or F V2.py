import time


def decoration(text, x):
    sides = "~" * 4
    formatted_text = f"{sides}{text}{sides}"
    if x == 1:
        top_bottom = "*" * len(formatted_text)
    elif x == 2:
        top_bottom = "=" * len(formatted_text)
    elif x == 3:
        top_bottom = "-" * len(formatted_text)
    elif x == 4:
        top_bottom = "#" * len(formatted_text)
    return print(f"{top_bottom}\n{formatted_text}\n{top_bottom}\n")


def yes_no_checker(question):
    while True:
        ans = input(question).lower()
        while ans not in ("y", "yes", "n", "no"):
            ans = input(question).lower()
        else:
            if ans in ("y", "yes"):
                return "yes"
            elif ans in ("n", "no"):
                return "no"


def instructions(game):
    if game == 1:
        if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
            decoration("Instructions", 2)
            print("\nYou will be given three options of games to play to help "
                  "you learn Maori\n\nEach game has a different style of "
                  "questioning as seen by their names\n\nTo choose which game "
                  "you want to play type the corresponding number next to the "
                  "game\n\nEach game will give the instructions on how to play "
                  "their game")
            print("="*62)
            waiting()
    elif game == 2:
        if yes_no_checker("Have you played True or False before?: ") == "no":
            decoration("Instructions", 2)
            print("\nYou will be given a statement and you will decide "
                  "whether it is true or false.\nTo decide you can input T or "
                  "True and F or False.\n\nEach question you get right will "
                  "award you a point.\nOnce all questions have been answered "
                  "the program will show a score out of 10.")
            print("="*78)
            waiting()

    elif game == 3:
        if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
            decoration("Instructions", 2)
            print("\nYou will be given three options of games to play to help "
                  "you learn Maori\n\nEach game has a different style of "
                  "questioning as seen by their names\n\nTo choose which game "
                  "you want to play type the corresponding number next to the "
                  "game\n\nEach game will give the instructions on how to play "
                  "their game")
            print("="*62)
            waiting()
    elif game == 4:
        if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
            decoration("Instructions", 2)
            print("\nYou will be given three options of games to play to help "
                  "you learn Maori\n\nEach game has a different style of "
                  "questioning as seen by their names\n\nTo choose which game "
                  "you want to play type the corresponding number next to the "
                  "game\n\nEach game will give the instructions on how to play "
                  "their game")
            print("="*62)
            waiting()


def waiting():
    if yes_no_checker("Are you ready to play?:") == "no":
        print("Ok i'll wait")
        wait = 1
        while wait != 5:
            print(".")
            time.sleep(1)
            wait += 1
        if yes_no_checker("Are you ready to play now?:") == "no":
            print("\nI'm not waiting any longer!")
            quit()


def true_or_false(question, answer, number):
    print(f"Question {number}:")
    player_answer = input(f"{question}\n").lower()
    while player_answer not in ("t", "true", "f", "false"):
        player_answer = input(f"{question}\n").lower()
    else:
        if player_answer in ("t", "true"):
            player_answer = "t"
        else:
            player_answer = "f"
    if player_answer == answer:
        decoration("CORRECT", 1)
    else:
        decoration("Wrong", 3)


instructions(2)
true_or_false("Rua means two", "t", 1)
true_or_false("Rua means three", "f", 2)
