def hangman():
    word_list = ["alcohol", "bitch", "clitoris", "dick", "erection", "fuck", "grip", "hunter",
            "irrumatio", "jk", "kitchen", "lotion", "mat", "newyork", "oppai", "playboy", "quiet",
            "rotation", "sex", "tongue", "up", "video", "wet", "xvideo", "yet", "zone"]
    import random
    word_index = random.randint(0, 25)
    word = word_list[word_index]
    wrong = 0
    stages = ["",
               "_____     ",
               "|         ",
               "|    |    ",
               "|    0    ",
               "|   /|)   ",
               "|   / |   ",
               "|_________"
               ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))
