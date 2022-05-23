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


def play_again(score, total):
    player_choice = input("Chose one of these options:\n1 - True or "
                          "False\n2 - Multiple Choice\n3 - Whole word answers"
                          "\n4 - Results\n")
    while player_choice not in ("1", "2", "3", "4"):
        player_choice = input("Please choose from a number from 1 - 4\n")
    if player_choice == "1":
        print("true or false")
        # t_or_f()
    elif player_choice == "2":
        print("multiple choice")
        # m_choice()
    elif player_choice == "3":
        print("whole word answers")
        # w_word()
    else:
        print(f"you scored {score}/{total}")


# Main Routine
play_again(45, 60)
