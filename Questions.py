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
    t_or_f_score += t_or_f("Rua means Two", "t", 1)
    t_or_f_score += t_or_f("Wha means Three", "f", 2)
    t_or_f_score += t_or_f("Food means Kai", "t", 3)
    t_or_f_score += t_or_f("Aporo means Apple", "t", 4)
    t_or_f_score += t_or_f("Sheep means Kau", "f", 5)
    t_or_f_score += t_or_f("Kunekune means Pig", "t", 6)
    t_or_f_score += t_or_f("Kikorangi means Blue", "t", 7)
    t_or_f_score += t_or_f("Yellow means Kakariki", "f", 8)
    t_or_f_score += t_or_f("Raspberry means Karepe", "f", 9)
    t_or_f_score += t_or_f("Beans means Pini", "t", 10)
    return t_or_f_score


def multiple_choice():
    m_score = 0
    m_score += m_choice("Five means?", "Rima", "Tahi", "Rua",
                        "Iwa", 1)
    m_score += m_choice("Karaka means?", "Orange", "Apple", "Cracker",
                        "Car", 2)
    m_score += m_choice("Block means?", "Paraka", "Kunekune", "Tokena",
                        "Kurupae", 3)
    m_score += m_choice("Ngaro means?", "Lost", "Forest", "Orange", "Gum", 4)
    m_score += m_choice("Whutupōro means?", "Rugby", "Football", "Tennis",
                        "Shot-put", 5)
    m_score += m_choice("Football means?", "Whutuporo", "Poi Kupenga", "Hoki",
                        "Hopukanga", 6)
    m_score += m_choice("Monument means?", "Whakamaharatanga", "Hākari",
                        "Whakapakoko", "Whakamaorihia", 7)
    m_score += m_choice("Mahau means?", "Hut", "Farm", "House", "River", 8)
    m_score += m_choice("Farm means?", "Pamu", "Moana", "Mara", "Oneone", 9)
    m_score += m_choice("English means?", "Reo Pakeha", "Reo Paniora",
                        "Reo Kariki", "Huanui", 10)
    return m_score


def whole_word_answers():
    w_score = 0
    w_score += w_word("What is Rua in English?", "two", 1)
    w_score += w_word("What is Nine in Maori?", "iwa", 2)
    w_score += w_word("What is Tekau in English?", "ten", 3)
    w_score += w_word("What is Waru in English?", "eight", 4)
    w_score += w_word("What is one in Maori?", "tahi", 5)
    w_score += w_word("What is Seven in Maori?", "whitu", 6)
    w_score += w_word("What is Five in Maori?", "rima", 7)
    w_score += w_word("What is Toru in English?", "three", 8)
    w_score += w_word("What is Ono in English?", "six", 9)
    w_score += w_word("What is Four in Maori?", "wha", 10)
    return w_score
