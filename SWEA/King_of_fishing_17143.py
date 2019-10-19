from collections import deque
import sys
sys.stdin = open("sample_input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def fishing(y: int):
    global ans, theMap
    for x in range(R):
        if theMap[x][y]:
            ans += theMap[x][y][0][2]
            theMap[x][y] = deque()
            break

    newMap = []
    for _ in range(R):
        tmp = []
        for _ in range(C):
            tmp.append(deque())
        newMap.append(tmp)

    for i in range(R):
        for j in range(C):
            if theMap[i][j]:
                speed = theMap[i][j][0][0]
                dir = theMap[i][j][0][1]
                size = theMap[i][j][0][2]
                nx, ny = i + speed * dx[dir], j + speed * dy[dir]
                if dir == 0 or dir == 1:
                    ny = j
                    if nx < 0 or nx >= R:
                        nx = abs(nx)
                        if (nx // (R - 1)) % 2 == 0:
                            dir = 1
                            nx = 0 + (nx % (R - 1))
                        else:
                            dir = 0
                            nx = R - 1 - (nx % (R - 1))
                else:
                    nx = i
                    if ny < 0 or ny >= C:
                        ny = abs(ny)
                        if ny // (C - 1) % 2 == 0:
                            dir = 2
                            ny = ny % (C - 1)
                        else:
                            dir = 3
                            ny = C - 1 - ( ny % (C - 1) )

                if newMap[nx][ny]:
                    if newMap[nx][ny][0][2] < size:
                        newMap[nx][ny].pop()
                        newMap[nx][ny].append([speed, dir, size])
                else:
                    newMap[nx][ny].append([speed, dir, size])
    theMap = newMap


R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    sharks.append([tmp[0] - 1, tmp[1] - 1, tmp[2], tmp[3] - 1, tmp[4]])

theMap = []
for _ in range(R):
    tmp = []
    for _ in range(C):
        tmp.append(deque())
    theMap.append(tmp)

for sh in sharks:
    theMap[sh[0]][sh[1]].append([sh[2], sh[3], sh[4]])

ans = 0
for y in range(C):
    fishing(y)
print(ans)