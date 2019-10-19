import sys

sys.stdin = open("sample_input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def one():
    global D, rx, ry
    D = (D - 1) % 4
    rx += dx[D]
    ry += dy[D]
    theMap[rx][ry] = 5

def two():
    global D
    D = (D - 1) % 4

def three():
    global D, rx, ry
    rx -= dx[D]
    ry -= dy[D]


N, M = map(int, input().split())
rx, ry, D = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))
theMap[rx][ry] = 5

while True:
    left = (D - 1) % 4
    behind = (D - 2) % 4
    right = (D + 1) % 4
    lx = rx + dx[left]
    ly = ry + dy[left]
    bx = rx + dx[behind]
    by = ry + dy[behind]
    kx = rx + dx[right]
    ky = ry + dy[right]
    fx = rx + dx[D]
    fy = ry + dy[D]

    if theMap[lx][ly] == 0:
        one()
    else:
        if (theMap[kx][ky] == 5 or theMap[kx][ky] == 1) and \
                (theMap[fx][fy] == 5 or theMap[fx][fy] == 1):
            if theMap[bx][by] == 1:
                break
            elif theMap[bx][by] == 5:
                three()
            else:
                two()
        else:
            two()

ret = 0
for x in range(N):
    for y in range(M):
        if theMap[x][y] == 5:
            ret += 1
print(ret)