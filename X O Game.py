import time

mat = [[1,2,3],[4,5,6],[7,8,9]]
# Matrix Function Codes
def show(mat):
    print("_______________")
    for o in range(0,3):
        for n in range(0,3):
            print("|",mat[o][n],"",end = "|")
        print("")
        print("_______________")

# Play Function Codes

turn=""
def play(mat,turn,num):
    for x in range(3):
        for y in range(3):
            if mat[x][y] == num:
                mat[x][y] = turn

# Win Function Codes

y = 0
def win(mat):
    # Row
    for x in range(3):
        if mat[x][y] == mat[x][y+1] == mat[x][y+2]:
            show(mat)
            print(mat[x][y],"Wins")
            print("Game Over")
            time.sleep(5.0)
            exit()
    # Column
    for x in range(3):
        if mat[y][x] == mat[y+1][x] == mat[y+2][x]:
            show(mat)
            print(mat[y][x], "Wins")
            print("Game Over")
            time.sleep(5.0)
            exit()
    # Diagonals
    if mat[0][0] == mat[1][1] == mat[2][2]:
        show(mat)
        print(mat[0][0], "Wins")
        print("Game Over")
        time.sleep(5.0)
        exit()
    if mat[0][2] == mat[1][1] == mat[2][0]:
        show(mat)
        print("Game Over")
        time.sleep(5.0)
        exit()

# Game Loop Statment Codes
while True:
    show(mat)
    if turn=="" :
        turn = input("Enter X or O : ")
        if turn != "X" and turn != "O":
            print("\nPlease enter a valid value")
            turn=""
            continue
    try:
        num = int(input(turn, "turn, Enter a Number : "))
    except ValueError:
        print("\nYou can only enter integers\n")
        show(mat)
        num = int(input(turn, "turn, Enter a Number : "))
    play(mat, turn, num)
    if turn == "X":
        turn="O"
    elif turn == "O":
        turn="X"
    win(mat)
