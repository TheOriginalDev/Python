import random
game=[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ladder = {2: 23, 8: 34, 20: 77, 32: 68, 41: 79, 74: 88, 85: 95, 82: 100}
snake = {29: 9, 38: 15, 47: 5, 53: 33, 62: 37, 97: 25, 86: 54, 92: 70}
p1 = 0
p2 = 0
player1 = "Amogh"
player2 = "Raj"
t = 1
print(game[0], "|", game[1], "|", game[2], "|", game[3], "|", game[4], "|", game[5], game[6], "|", game[7], "|", game[8], "|", game[9])
print("-" * 50)
print(game[10], "|", game[11], "|", game[12], "|", game[13], "|", game[14], "|", game[15], game[16], "|", game[17], "|", game[18], "|", game[19])
print("-" * 50)
print(game[20], "|", game[21], "|", game[22], "|", game[23], "|", game[24], "|", game[25], game[26], "|", game[27], "|", game[28], "|", game[29])
print("-" * 50)
print(game[30], "|", game[31], "|", game[32], "|", game[33], "|", game[34], "|", game[35], "|", game[36], "|", game[37], "|", game[38], "|", game[39])
print("-" * 50)
print(game[40], "|", game[41], "|", game[42], "|", game[43], "|", game[44], "|", game[45], "|", game[46], "|", game[47], "|", game[48], "|", game[49])
print("-" * 50)
print(game[40], "|", game[41], "|", game[42], "|", game[43], "|", game[44], "|", game[45], "|", game[46], "|", game[47], "|", game[48], "|", game[49])
print("-" * 50)
print(game[50], "|", game[51], "|", game[52], "|", game[53], "|", game[54], "|", game[55], "|", game[56], "|", game[57], "|", game[58], "|", game[59])
print("-" * 50)
print(game[60], "|", game[61], "|", game[62], "|", game[63], "|", game[64], "|", game[65], "|", game[66], "|", game[67], "|", game[68], "|", game[69])
print("-" * 50)
print(game[70], "|", game[71], "|", game[72], "|", game[73], "|", game[74], "|", game[75], "|", game[76], "|", game[77], "|", game[78], "|", game[79])
print("-" * 50)
print(game[80], "|", game[81], "|", game[82], "|", game[83], "|", game[84], "|", game[85], "|", game[86], "|", game[87], "|", game[88], "|", game[89])
print("-" * 50)
print(game[90], "|", game[91], "|", game[92], "|", game[93], "|", game[94], "|", game[95], "|", game[96], "|", game[97], "|", game[98], "|", game[99])
print("-" * 50)
while p1 < 100 and p2 < 100:
    if t % 2 == 0:
        print("***********************************")
        print(player2, "your turn")
        d1 = random.randint(1, 6)
        x = input("Press Enter")
        print("Your Dice ", x)
        p2 = p2 + d1
        print("You are on ", p2)



        if p2 in ladder:
            p2 = ladder[p2]
            print("Yayy, there is a ladder, you are now on ", p1)
        elif p2 in snake:
            p2 = snake[p2]
            print("Ohh no snake is there now u are on ", p1)

        elif p1 in ladder:
            p1 = ladder[p1]
            print("Yayy, there is a ladder, you are now on ", p1)
        elif p1 in snake:
            p1 = snake[p1]
            print("Oh no, there is a snake, now you are on ", p1)

    else:
        print(player1, "ur turn")
        d1 = random.randint(1, 6)
        x = input("Press Enter ")
        print("your dice ", x)
        p1 = p1 + d1
        print("You are on", p1)
    t = t + 1
if p1 > 100:
    print(player1, "is winner")
else:
    print(player2, "is winner")