def hangman(word):
    wrong = 0
    success = 0
    stages = [ '',
               '__________          ',
               '                    ',
               '          |         ',
               '          0         ',
               '         /|\        ',
               '         / \        ',
               '                    ']
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to Hangman...")
    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter!\n"
        char = input(msg)
        for i, let in enumerate(rletters):
            if let == char:
                success += 1
                board[i] = char
        if success == 0:
            wrong += 1
        success = 0
        print((" ".join(board)))
        e = wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
        if wrong == len(stages) - 1:
            print("\n".join(stages[0:wrong]))
            print("You lose! It was {}.".format(word))

#words = [
#import random
#word = words[random.randint(0,len(words)-1)]
#word =" "
#hangman(word)
