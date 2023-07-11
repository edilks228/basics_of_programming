black = 2
pole = [[0,0,0,0,0,0,0,0],
        [0,0,2,0,2,0,2,0],
        [0,0,0,0,0,0,0,0],
        [0,0,2,0,2,0,2,0],
        [0,0,0,1,0,0,0,0],
        [0,0,2,0,2,0,2,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

def Count(i,j):
    a = [0] * 4
    if i > 2 and j > 2 and pole[i-1][j-1] == black and pole[i-2][j-2] == 0:
        pole[i-1][j-1] = 0
        a[0] = 1 + Count(i-2,j-2)
        pole[i-1][j-1] = black

    if i < 7 and j < 7 and pole[i+1][j+1] == black and pole[i+1][j+1] == 0:
        pole[i + 1][j + 1] = 0
        a[1] = 1 + Count(i+2,j+2)
        pole[i+1][j+1] = black

    if i > 2 and j < 7 and pole[i-1][j+1] == black and pole[i-2][j+1] == 0:
        pole[i-1][j+1] = 0
        a[2] = 1 + Count(i-2,j+2)
        pole[i-1][j-1] = black

    if i < 7 and j > 2 and pole[i+1][j-1] == black and pole[i+2][j-2] == 0:
        pole[i + 1][j - 1] = 0
        a[3] = 1 + Count(i + 2, j - 2)
        pole[i + 1][j - 1] = black

    z = a[0]
    for k in range(4):
        if a[k] > z:
            z = a[k]
    return z

print(Count(4,3))
