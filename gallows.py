import random

def hangman():
    word_list = ["хакер","взлом","программа","вирус","кот","собака","cуществительное","прилагательное","волк","мангуст","компьютер","лев","турция","смерть","роды","жильё","квартира","дача"]
    random_number = random.randint(0, 18)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
            "________      ",
            "|             ",
            "|       |     ",       # Визуальная часть игры, подготовка переменных
            "|       0     ",
            "|      /|\    ",
            "|      / \    ",
            "|             "
            ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    print("Все слова русские и с маленькой буквой !")
    while wrong < len(stages)-1:
        print("\n")
        msg = "Введите букву:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) # Реализация цикла игры
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выграли! Было загадоно слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загадоно слово: {}.".format(word))




hangman()


