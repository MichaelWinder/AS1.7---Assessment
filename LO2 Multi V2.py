import time
import random


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
    elif x == 0:
        formatted_text = text
        top_bottom = "=" * len(formatted_text)
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
            print("=" * 62)
            waiting()
    elif game == 2:
        if yes_no_checker("Have you played True or False before?: ") == "no":
            decoration("Instructions", 2)
            print("\nYou will be given a statement and you will decide "
                  "whether it is true or false.\nTo decide you can input T or "
                  "True and F or False.\n\nEach question you get right will "
                  "award you a point.\nOnce all questions have been answered "
                  "the program will show a score out of 20.")
            print("=" * 78)
            waiting()

    elif game == 3:
        if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
            decoration("Instructions", 2)
            print("You will be given a question and four different "
                  "possible answers\nYour job is to decide which is the "
                  "right answer\nTo do that each answer will have a number "
                  "next to it\n\n"
                  "Input that number to choose that answer Each question you "
                  "get right will award you a point\nOnce all questions have "
                  "been answered the program will show a score out of 20")
            print("=" * 77)
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
            print("=" * 62)
            waiting()


# This code is here for the player's entertainment
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


# Runs the multiple choice questions
def m_choice(question, answer, blank1, blank2, blank3, number):
    instructions(3)
    answer_randomiser = [answer, blank1, blank2, blank3]
    list_number = random.randint(0, 3)
    option_one = answer_randomiser.pop(list_number)
    list_number = random.randint(0, 2)
    option_two = answer_randomiser.pop(list_number)
    list_number = random.randint(0, 1)
    option_three = answer_randomiser.pop(list_number)
    option_four = answer_randomiser[0]
    print(f"Question {number}:")
    player_answer = input(f"{question}\n1 - {option_one}\n2 - {option_two}\n"
                          f"3 - {option_three}\n4 - {option_four}\n")
    while player_answer not in ("1", "2", "3", "4"):
        player_answer = input("Answer either 1 2 3 or 4"
                              f"\n{question}\n{option_one}\n{option_two}\n"
                              f"{option_three}\n{option_four}\n")
    if player_answer == "1" and option_one == answer:
        decoration("CORRECT", 1)
        return 1
    elif player_answer == "2" and option_two == answer:
        decoration("CORRECT", 1)
        return 1
    elif player_answer == "3" and option_three == answer:
        decoration("CORRECT", 1)
        return 1
    elif player_answer == "4" and option_four == answer:
        decoration("CORRECT", 1)
        return 1
    else:
        decoration("Wrong", 3)
        return 0


# Main Routine
m_score = 0

# Questions
m_score += m_choice("What is five in Maori?", "Rima", "Tahi", "Rua", "Iwa", 1)

# Overall score
decoration(f"You scored {m_score}/20", 0)
