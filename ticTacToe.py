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

end = False
printDisplay()
while(not end):
    x = input("player x type coordinate (x,y)")
    coordinates = x.split(",")
    drawSymbol(int(coordinates[0])-1,int(coordinates[1])-1,"x")
    for i in range(4):
        print()
    printDisplay()
    o = input("player o type coordinate (x,y)")
    coordinates = o.split(",")
    drawSymbol(int(coordinates[0])-1, int(coordinates[1])-1, "o")
    for i in range(4):
        print()
    printDisplay()

#change