import random

game = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))
ladder={2:23, 8:34, 20:77, 32:68, 41:79, 74:88, 85:95, 82:100}
snake={29:9, 38:15, 47:5, 53:33, 62:37, 97:25, 86:54, 92:70}


turn = 1
while turn < 99:
    if turn % 2 == 0:
        pos = random.choice(dice)
        print("Amogh your value is =>", pos)
        turn = turn + pos
    else:
        pos = random.choice(dice)
        print("Shyam your value is =>", pos)
        turn=turn+pos

    print("After", turn, "value")
    print(game[0], "|", game[1], "|", game[2], game[3], "|", game[4], "|", game[5], game[6], "|", game[7], "|", game[8],
          "|", game[9])
    print("-" * 10)
    print(game[10], "|", game[11], "|", game[12], game[13], "|", game[14], "|", game[15], game[16], "|", game[17], "|",
          game[18], "|", game[19])
    print("-" * 10)
    print(game[20], "|", game[21], "|", game[22], game[23], "|", game[24], "|", game[25], game[26], "|", game[27], "|",
          game[28], "|", game[29])
    print("-" * 10)
    print(game[30], "|", game[31], "|", game[32], game[33], "|", game[34], "|", game[35], game[36], "|", game[37], "|",
          game[38], "|", game[39])
    print("-" * 10)
    print(game[40], "|", game[41], "|", game[42], game[43], "|", game[44], "|", game[45], game[46], "|", game[47], "|",
          game[48], "|", game[49])
    print("-" * 10)
    print(game[40], "|", game[41], "|", game[42], game[43], "|", game[44], "|", game[45], game[46], "|", game[47], "|",
          game[48], "|", game[49])
    print("-" * 10)
    print(game[50], "|", game[51], "|", game[52], game[53], "|", game[54], "|", game[55], game[56], "|", game[57], "|",
          game[58], "|", game[59])
    print("-" * 10)
    print(game[60], "|", game[61], "|", game[62], game[63], "|", game[64], "|", game[65], game[66], "|", game[67], "|",
          game[68], "|", game[69])
    print("-" * 10)
    print(game[70], "|", game[71], "|", game[72], game[73], "|", game[74], "|", game[75], game[76], "|", game[77], "|",
          game[78], "|", game[79])
    print("-" * 10)
    print(game[80], "|", game[81], "|", game[82], game[83], "|", game[84], "|", game[85], game[86], "|", game[87], "|",
          game[88], "|", game[89])
    print("-" * 10)
    print(game[90], "|", game[91], "|", game[92], game[93], "|", game[94], "|", game[95], game[96], "|", game[97], "|",
          game[98], "|", game[99])