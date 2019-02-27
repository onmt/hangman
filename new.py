"""
単語当てゲーム「ハングマン」 2019/02/28

変数一覧:
    word        :正解となる単語
    wrong       :不正解の数
    stages      :ハングマンのアスキーアートのリスト。wrong < len(stages) - 1 でwhileを抜けゲーム終了
    rletters    :wordを一文字づつに分けたリスト
    board       :正解の単語を伏せ字にしたボード。正答すると伏せ字が表示される
    win         :勝ち負けのフラグ
    char        :ユーザーが入力した文字
    cind        :charがrlettersの何番目にあるかの番号


"""

import random

wordlist = ["cat", "dog", "duck", "elephant", "zebra", "monkey", "chopstick", "bottle", "mouse"]

i = len(wordlist)
word_number = random.randint(0, i - 1)
word = wordlist[word_number]


def hangman(word):
    wrong = 0
    stages = ["",
              "_________      ",
              "|              ",
              "|       |      ",
              "|       o      ",
              "|      /|L     ",
              "|      / >     ",
              "|              ",
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
            rletters[cind] = '$'  # 当てた箇所を$にすることで再び当てられないようにする
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
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は {}".format(word))


hangman(word)
