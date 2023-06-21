game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
turn = 1
while turn < 10:

    if turn % 2 == 0:
        pos = int(input("Amogh ur turn =>"))

        if game[pos - 1] == '_':
            game[pos - 1] = 'X'
        else:
            print("Taken")
            turn = turn - 1
    else:
        pos = int(input("Shyam ur turn =>"))
        if game[pos - 1] == '_':
            game[pos - 1] = '0'
        else:
            print("Taken")
            turn = turn - 1

    print("After", turn, "value")
    print(game[0], "|", game[1], "|", game[2])
    print("-" * 10)
    print(game[3], "|", game[4], "|", game[5])
    print("-" * 10)
    print(game[6], "|", game[7], "|", game[8])
    print("-" * 10)

    if game[0] == game[1] and game[0] == game[2] and game[0] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[0] == game[1] and game[0] == game[2] and game[0] == "0":
        print("Shyam is winner")
        turn = 42
    elif game[3] == game[4] and game[3] == game[5] and game[3] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[3] == game[4] and game[3] == game[5] and game[3] == "0":
        print("Shyam is winner")
        turn = 42
    elif game[6] == game[7] and game[6] == game[8] and game[6] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[6] == game[7] and game[6] == game[8] and game[6] == "0":
        print("Shyam is winner")
        turn = 42
    elif game[0] == game[4] and game[0] == game[8] and game[0] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[0] == game[4] and game[0] == game[8] and game[0] == "O":
        print("Shyam is winner")
        turn = 42
    elif game[2] == game[4] and game[2] == game[6] and game[2] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[2] == game[4] and game[2] == game[6] and game[2] == "0":
        print("Shyam is winner")
        turn = 42
    elif game[0] == game[3] and game[0] == game[6] and game[0] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[0] == game[3] and game[0] == game[6] and game[0] == "0":
        print("Shyam is winner")
        turn = 42
    elif game[1] == game[4] and game[1] == game[7] and game[1] == "X":
        print("Amogh is winner")
        turn = 42
    elif game[1] == game[4] and game[1] == game[7] and game[1] == "0":
        print("Shyam is winner")
        turn = 42
    elif game[2] == game[5] and game[2] == game[8] and game[2] == "X":
        print("Amogh is winner")
        turn = 42

    turn = turn + 1

if turn == 10:
    print("It's' a tie")
