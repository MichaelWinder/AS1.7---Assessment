"""This code asks for the players name, tells the player instructions if
they want them, and gives 3 options of games to play"""
import time


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


# Shows player instructions
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
    return print(f"{top_bottom}\n{formatted_text}\n{top_bottom}")


# Choosing what game to play and running it
def choosing_game():
    print("1 - True or False\n2 - Multiple Choice"
          "\n3 - Whole word answers")
    game_choice = input("What game would you like to play?:")
    while game_choice not in ("1", "2", "3"):
        game_choice = input("What game would you like to play?"
                            "(1, 2, or 3):")
    if game_choice == "1":
        print("true")
        # true_or_false()
    elif game_choice == "2":
        print("multiple")
        # multiple_choice()
    else:
        print("whole")
        # whole_word_answers()


# Main Routine
decoration("Welcome to the Maori Quiz!", 1)
name = input("Hello what is your name: ").capitalize()
print(f"Well {name} I hope you enjoy learning Maori!\n")
instructions()
choosing_game()
