import random
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
                  "game\n\nEach game will give the instructions on how to "
                  "play their game")
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
        if yes_no_checker("Have you played Multiple Choice before?: ") == "no":
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
        if yes_no_checker("Have you played Whole Word Answers before?: ") ==\
                "no":
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


# Choosing what game to play and running it
def choosing_game():
    print("1 - True or False\n2 - Multiple Choice"
          "\n3 - Whole word answers")
    game_choice = input("What game would you like to play?:")
    while game_choice not in ("1", "2", "3"):
        game_choice = input("What game would you like to play?"
                            "(1, 2, or 3):")
    if game_choice == "1":
        t_or_f_score = true_or_false()
        decoration(f"You scored {t_or_f_score}/20", 0)
        return t_or_f_score
    elif game_choice == "2":
        m_score = multiple_choice()
        decoration(f"You scored {m_score}/20", 0)
        return m_score
    else:
        w_score = whole_word_answers()
        decoration(f"You scored {w_score}/20", 0)
        return w_score


# Presents a statement and tells whether player answer is correct or not
def t_or_f(question, answer, number):
    print(f"Question {number}:")
    player_answer = input(f"{question}\n").lower()
    while player_answer not in ("t", "true", "f", "false"):
        player_answer = input(f"Answer either true or fal"
                              f"se\n{question}\n").lower()
    else:
        if player_answer in ("t", "true"):
            player_answer = "t"
        else:
            player_answer = "f"
    if player_answer == answer:
        decoration("CORRECT", 1)
        return 1
    else:
        decoration("Wrong", 3)
        return 0


# Asks a question and shows 4 different answers
def m_choice(question, answer, blank1, blank2, blank3, number):
    instructions(3)
    answer_randomiser = [answer, blank1, blank2, blank3]
    random.shuffle(answer_randomiser)
    option_one = answer_randomiser.pop(0)
    option_two = answer_randomiser.pop(0)
    option_three = answer_randomiser.pop(0)
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


# Asks a question and expects a whole word answer
def w_word(question, answer, number):
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


# Player can play another game or end and get results
def play_again(score, total):
    player_choice = input("To play again chose one of these "
                          "options:\n1 - True or "
                          "False\n2 - Multiple Choice\n3 - Whole word answers"
                          "\n4 - Results\n")
    while player_choice not in ("1", "2", "3", "4"):
        player_choice = input("Please choose from a number from 1 - 4\n")
    if player_choice == "1":
        t_or_f_score = true_or_false()
        decoration(f"You scored {t_or_f_score}/20", 0)
        return t_or_f_score
    elif player_choice == "2":
        m_score = multiple_choice()
        decoration(f"You scored {m_score}/20", 0)
        return m_score
    elif player_choice == "3":
        w_score = whole_word_answers()
        decoration(f"You scored {w_score}/20", 0)
        return w_score
    else:
        print(f"You scored {score}/{total}")
        quit()


def true_or_false():
    instructions(2)
    t_or_f_score = 0
    t_or_f_score += t_or_f("Rua means two", "t", 1)
    t_or_f_score += t_or_f("Rua means three", "f", 2)
    return t_or_f_score


def multiple_choice():
    instructions(3)
    m_score = 0
    m_score += m_choice("What is five in Maori?", "Rima", "Tahi", "Rua",
                        "Iwa", 1)
    return m_score


def whole_word_answers():
    instructions(4)
    w_score = 0
    w_score += w_word("What is Rua in English?", "two", 1)
    return w_score


# Main Routine
decoration("Welcome to the Maori Quiz!", 1)
name = input("Hello what is your name: ").capitalize()
print(f"Well {name} I hope you enjoy learning Maori!\n")
instructions(1)
total = 20
score = 0
score += choosing_game()

while True:
    score += play_again(score, total)
    total += 20
