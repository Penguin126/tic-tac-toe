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
    try:
        int(x + y)
    except ValueError:
        return False
    else:
        if int(x)>3 or int(x)<1 or int(y)>3 or int(y)<1:
            return False
        elif board[int(x)-1][int(y)-1]!=" ":
            return False
        else:
            return True

def checkEnd():
    for i in range(3):
        if board[i][0]=='x' and board[i][1]=='x' and board[i][2]=='x':
            return "x"
        elif board[i][0]=='o' and board[i][1]=='o' and board[i][2]=='o':
            return "o"
    for i in range(3):
        if board[0][i]=='x' and board[1][i]=='x' and board[2][i]=='x':
            return "x"
        elif board[0][i]=='o' and board[1][i]=='o' and board[2][i]=='o':
            return "o"
    if board[0][0]=='x' and board[1][1]=='x' and board[2][2]=='x':
        return "x"
    elif board[0][0]=='o' and board[1][1]=='o' and board[2][2]=='o':
        return "o"
    if board[0][2]=='x' and board[1][1]=='x' and board[2][0]=='x':
        return "x"
    elif board[0][2]=='o' and board[1][1]=='o' and board[2][0]=='o':
        return  "o"
    if count>=9:
        return " "

count = 0
printDisplay()
while(True):
    while(True):
        x = input("player x type coordinate (row,col): ")
        coordinates = x.split(",")
        if isLegal(coordinates[0],coordinates[1],"x",board):
            drawSymbol(int(coordinates[0])-1,int(coordinates[1])-1,"x")
            board[int(coordinates[0])-1][int(coordinates[1])-1] = "x"
            for i in range(4):
                print()
            printDisplay()
            break
        else:
            print("invalid input!")
    count+=1
    if checkEnd() == " ":
        print("Tie!")
        break
    elif checkEnd() == "x":
        print("Player x wins!")
        break
    elif checkEnd() == "o":
        print("Player o wins!")
        break
    while(True):
        o = input("player o type coordinate (row,col): ")
        coordinates = o.split(",")
        if isLegal(coordinates[0],coordinates[1],"o",board):
            drawSymbol(int(coordinates[0])-1, int(coordinates[1])-1, "o")
            board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "o"
            for i in range(4):
                print()
            printDisplay()
            break
        else:
            print("invalid input!")
    count+=1
    if checkEnd() == " ":
        print("Tie!")
        break
    elif checkEnd() == "x":
        print("Player x wins!")
        break
    elif checkEnd() == "o":
        print("Player o wins!")
        break

#change
#git status
#git add <file>
#git commit -m "mrdgr"
#git push origin