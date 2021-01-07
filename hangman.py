import random
my_list=["cat","dog","bird","tiger","bull","rabit","fish","whale"]
def hangman(word):
 wrong=0
 stages=["",
         "________        ",
         "|               ",
         "|        |      ",
         "|        O      ",
         "|       /|\     ",
         "|       / \     ",
         "|               "
         ]
 rletters=list(word)
 board=["_"]*len(word)
 win = False
 print("Welcome to Hangman!")

 while wrong < len(stages)-1:
     print("\n")
     msg="guess a word"
     char=input(msg)
     if char in rletters:
        cind=rletters.index(char)
        board[cind]=char
        rletters[cind]='$'
     else:
        wrong+=1
     print(" ".join(board))
     e=wrong+1
     print("\n".join(stages[0:e]))
     if "_" not in board:
        print("you are winner!")
        print(" ".join(board))
        win=True
        break
 if not win:
    print("\n".join(stages[0:wrong+1]))
    print("you lose!the answer is {}.".format(word))

hangman(my_list[random.randint(0,7)])