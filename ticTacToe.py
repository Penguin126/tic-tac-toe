board = [[" "] * 3 for i in range(3)]
display = [[" "] * 30 for i in range(30)]
for i in range(30):
    display[10][i] = "_"
for i in range(30):
    display[20][i] = "_"
for i in range(30):
    display[i][10] = "|"
for i in range(30):
    display[i][20] = "|"
def printDisplay():
    for i in range(30):
        for n in range(30):
            print(display[i][n], end = "  ")
        print()
def drawSymbol(r,c,symbol):
    srow = r*10+1
    scol = c*10+1
    if symbol == "x":
        for i in range(9):
            display[srow+i][scol+i] = "x"
        for i in range(9):
            display[srow+i][scol+8-i] = "x"
    elif symbol == "o":
        display[srow+1][scol+1] = "o"
        display[srow+1][scol+7] = "o"
        display[srow+7][scol+1] = "o"
        display[srow+7][scol+7] = "o"
        for i in range(5):
            display[srow][scol+2+i] = "o"
        for i in range(5):
            display[srow+8][scol+2+i] = "o"
        for i in range(5):
            display[srow+2+i][scol] = "o"
        for i in range(5):
            display[srow+2+i][scol+8] = "o"
def isLegal(x,y,symbol,board):
    if x>2 or x<0 or y>2 or y<0:
        return False
    elif board[x][y]!=" ":
        return False
    else:
        return True
end = False
printDisplay()
while(not end):
    while(True):
        x = input("player x type coordinate (row,col): ")
        coordinates = x.split(",")
        if isLegal(int(coordinates[0])-1,int(coordinates[1])-1,"x",board):
            drawSymbol(int(coordinates[0])-1,int(coordinates[1])-1,"x")
            board[int(coordinates[0])-1][int(coordinates[1])-1] = "x"
            for i in range(4):
                print()
            printDisplay()
            break
        else:
            print("invalid input!")
    while(True):
        o = input("player o type coordinate (row,col): ")
        coordinates = o.split(",")
        if isLegal(int(coordinates[0])-1,int(coordinates[1])-1,"o",board):
            drawSymbol(int(coordinates[0])-1, int(coordinates[1])-1, "o")
            board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "o"
            for i in range(4):
                print()
            printDisplay()
            break
        else:
            print("invalid input!")

#change
#git status
#git add <file>
#git commit -m "mrdgr"
#git push origin