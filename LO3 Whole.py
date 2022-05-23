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
            print("You will be given three options of games to play to help "
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
            print("You will be given a statement and you will decide "
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
                  "right answer\n\nTo do that each answer will have a number "
                  "next to it\nInput that number to choose that "
                  "answer\n\nEach question you "
                  "get right will award you a point\nOnce all questions have "
                  "been answered the program will show a score out of 20")
            print("=" * 77)
            waiting()
    elif game == 4:
        if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
            decoration("Instructions", 2)
            print("You will be given a question that you will have to "
                  "answer a whole word (not numbers)\nIf you get the "
                  "question wrong you are given a second chance to "
                  "answer\n\nEach question you get right will award you a "
                  "point.\nOnce all questions have been answered the "
                  "program will show a score out of 20.")
            print("=" * 78)
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


def w_word(question, answer, number):
    instructions(4)
    print(f"Question {number}:")
    player_answer = input(f"{question}\n").lower()
    if player_answer != answer:
        decoration("Wrong", 3)
        player_answer = input(f"Ill give a second chance\n"
                              f"{question}\n").lower()
    if player_answer == answer:
        decoration("CORRECT", 1)
        return 1
    else:
        decoration("Wrong", 3)
        return 0


# Main Routine
w_score = 0

# Questions
w_score += w_word("What is Rua in English?", "two", 1)
w_score += w_word("What is Rua in English?", "two", 2)

# Overall Score
decoration(f"You scored {w_score}/20", 0)
