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
def instructions():
    if yes_no_checker("Have you played this Maori Quiz before?: ") == "no":
        decoration("Instructions", 2)
    else:
        print("Program Continues")


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

instructions()
choosing_game()
