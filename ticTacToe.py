n = 30
m = 30
display = [[" "] * m for i in range(n)]
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
printDisplay()