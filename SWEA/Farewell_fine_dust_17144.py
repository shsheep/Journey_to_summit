import math
import sys

sys.stdin = open("sample_input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def spread():
    spMap = []
    for _ in range(R+2):
        tmp = []
        for _ in range(C+2):
            tmp.append(0)
        spMap.append(tmp)

    for x in range(1, R+1):
        for y in range(1, C+1):
            if theMap[x][y] <= 0:
                continue
            dust = math.trunc(theMap[x][y] / 5)
            numSpread = 0
            for dir in range(4):
                new_x = x + dx[dir]
                new_y = y + dy[dir]
                if theMap[new_x][new_y] < 0:
                    continue
                numSpread += 1
                spMap[new_x][new_y] += dust
            theMap[x][y] -= dust * numSpread
    for x in range(1, R+1):
        for y in range(1, C+1):
            theMap[x][y] += spMap[x][y]

def rotate():
    # Upper part - Counter-clockwise
    # Left
    for x in range(cleaner[0] - 1, 1, -1):
        theMap[x][1] = theMap[x-1][1]
    # Up
    for y in range(1, C):
        theMap[1][y] = theMap[1][y+1]
    # Right
    for x in range(1, cleaner[0]):
        theMap[x][C] = theMap[x+1][C]
    # Down
    for y in range(C, 1, -1):
        theMap[cleaner[0]][y] = theMap[cleaner[0]][y-1]
    theMap[cleaner[0]][2] = 0

    # Lower part - Clockwise
    # Left
    for x in range(cleaner[1] + 1, R):
        theMap[x][1] = theMap[x+1][1]
    # Down
    for y in range(1, C):
        theMap[R][y] = theMap[R][y+1]
    # Right
    for x in range(R, cleaner[1], -1):
        theMap[x][C] = theMap[x-1][C]
    # Up
    for y in range(C, 1, -1):
        theMap[cleaner[1]][y] = theMap[cleaner[1]][y-1]
    theMap[cleaner[1]][2] = 0

R, C, T = map(int, input().split())\

theMap = []
for _ in range(R):
    tmp = list(map(int, input().split()))
    theMap.append([-2] + tmp + [-2])
theMap = [[-2] * (C+2)] + theMap + [[-2] * (C+2)]

cleaner = []
for x in range(R+2):
    for y in range(C+2):
        if theMap[x][y] == -1:
            cleaner.append(x)

for _ in range(T):
    spread()
    rotate()

ret = 0
for x in range(1, R+1):
    ret += sum(theMap[x][1:-1])
ret += 2
print(ret)