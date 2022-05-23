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


def m_choice(question, answer, blank1, blank2, blank3, number):
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


def true_or_false():
    t_or_f_score = 0
    t_or_f_score += t_or_f("Rua means two", "t", 1)
    t_or_f_score += t_or_f("Rua means three", "f", 2)
    t_or_f_score += t_or_f("", "", 3)
    t_or_f_score += t_or_f("", "", 4)
    t_or_f_score += t_or_f("", "", 5)
    t_or_f_score += t_or_f("", "", 6)
    t_or_f_score += t_or_f("", "", 7)
    t_or_f_score += t_or_f("", "", 8)
    t_or_f_score += t_or_f("", "", 9)
    t_or_f_score += t_or_f("", "", 10)
    t_or_f_score += t_or_f("", "", 11)
    t_or_f_score += t_or_f("", "", 12)
    t_or_f_score += t_or_f("", "", 13)
    t_or_f_score += t_or_f("", "", 14)
    t_or_f_score += t_or_f("", "", 15)
    t_or_f_score += t_or_f("", "", 16)
    t_or_f_score += t_or_f("", "", 17)
    t_or_f_score += t_or_f("", "", 18)
    t_or_f_score += t_or_f("", "", 19)
    t_or_f_score += t_or_f("", "", 20)
    return t_or_f_score


def multiple_choice():
    m_score = 0
    m_score += m_choice("What is five in Maori?", "Rima", "Tahi", "Rua",
                        "Iwa", 1)
    m_score += m_choice("", "", "", "", "", 2)
    m_score += m_choice("", "", "", "", "", 3)
    m_score += m_choice("", "", "", "", "", 4)
    m_score += m_choice("", "", "", "", "", 5)
    m_score += m_choice("", "", "", "", "", 6)
    m_score += m_choice("", "", "", "", "", 7)
    m_score += m_choice("", "", "", "", "", 8)
    m_score += m_choice("", "", "", "", "", 9)
    m_score += m_choice("", "", "", "", "", 10)
    m_score += m_choice("", "", "", "", "", 11)
    m_score += m_choice("", "", "", "", "", 12)
    m_score += m_choice("", "", "", "", "", 13)
    m_score += m_choice("", "", "", "", "", 14)
    m_score += m_choice("", "", "", "", "", 15)
    m_score += m_choice("", "", "", "", "", 16)
    m_score += m_choice("", "", "", "", "", 17)
    m_score += m_choice("", "", "", "", "", 18)
    m_score += m_choice("", "", "", "", "", 19)
    m_score += m_choice("", "", "", "", "", 20)
    return m_score


def whole_word_answers():
    w_score = 0
    w_score += w_word("What is Rua in English?", "two", 1)
    w_score += w_word("?", "", 2)
    w_score += w_word("?", "", 3)
    w_score += w_word("?", "", 4)
    w_score += w_word("?", "", 5)
    w_score += w_word("?", "", 6)
    w_score += w_word("?", "", 7)
    w_score += w_word("?", "", 8)
    w_score += w_word("?", "", 9)
    w_score += w_word("?", "", 10)
    w_score += w_word("?", "", 11)
    w_score += w_word("?", "", 12)
    w_score += w_word("?", "", 13)
    w_score += w_word("?", "", 14)
    w_score += w_word("?", "", 15)
    w_score += w_word("?", "", 16)
    w_score += w_word("?", "", 17)
    w_score += w_word("?", "", 18)
    w_score += w_word("?", "", 19)
    w_score += w_word("?", "", 20)
    return w_score
