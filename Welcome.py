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
        print("Space for Instructions")


# Main Routine
print("Welcome to the Maori Quiz!\n")
name = input("Hello what is your name: ")
print(f"Well {name} I hope you enjoy learning Maori!\n")
instructions()
