''' The game is played on a rectangular grid with a given size. Some cells
contain power nodes. The rest of the cells are empty.
The goal is to find, when they exist, the horizontal and vertical neighbors of
each node. '''
x = []
y = []
X = Y = 0
NODE = ""
SPC = " "

width = int(input())
height = int(input())

for i in range(height):
    line = list(input())
    for j, ln in enumerate(line):
        if ln == "0":
            x.append(j)
            y.append(i)
LEN_LIST = len(x)

for i in range(LEN_LIST):
    X = x[i]
    Y = y[i]
    x[i] = y[i] = None
    NODE += str(X) + SPC + str(Y) + SPC

    if Y in y:
        idx = y.index(Y)
        NODE += str(x[idx]) + SPC + str(y[idx]) + SPC
    else:
        NODE += "-1 -1 "

    if X in x:
        idx = x.index(X)        
        NODE += str(x[idx]) + SPC + str(y[idx])
    else:
        NODE += "-1 -1"
    print(NODE, end="\n")
    NODE = ""
