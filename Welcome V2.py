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


def instructions():
    if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
        print("\n****How to play Maori Quiz****\n"
              "\nYou will be given three options of games to play to help you learn Maori\n"
              "\nEach game has a different style of questioning as seen by their names\n"
              "\nTo choose which game you want to play type the corresponding number next to the game\n"
              "\nEach game will give the instructions on how to play their game"
              "\n==============================================================")
        if yes_no_checker("Are you ready to play?:") == "no":
            print("Ok i'll wait")
            if yes_no_checker("Are you ready to play now?:") == "no":
                print("\nI'm not waiting any longer!")
                quit()


# Main Routine
print("Welcome to the Maori Quiz!\n")
name = input("Hello what is your name: ")
print(f"Well {name} I hope you enjoy learning Maori!\n")
instructions()


# Choosing what game to play
print("1 - True or False\n2 - Multiple Choice"
      "\n3 - Whole word answers")
game_choice = input("What game would you like to play?:")
while game_choice not in ("1", "2", "3"):
    game_choice = input("What game would you like to play?(1, 2, or 3):")
if game_choice == "1":
    print("1")
    # true_or_false()
elif game_choice == "2":
    print("2")
    # multiple_choice()
else:
    print("3")
    # whole_word_answers()
