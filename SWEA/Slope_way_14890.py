import sys

sys.stdin = open("sample_input.txt", "r")

N, L = map(int, input().split())
theMap = []
newMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))
    newMap.append([0] * N)
for x in range(N):
    for y in range(N):
        newMap[N - y - 1][x] = theMap[x][y]
theMap += newMap

ret = 0
j = 0
for i in range(2 * N):
    cnt = 1
    possible = True
    for j in range(N - 1):
        if theMap[i][j] == theMap[i][j+1]:
            cnt += 1
        elif theMap[i][j] + 1 == theMap[i][j+1] and cnt >= L:
            cnt = 1
        elif theMap[i][j] == theMap[i][j+1] + 1 and cnt >= 0:
            cnt = 1 - L
        else:
            possible = False
            break
    if possible and cnt >= 0:
        ret += 1
print(ret)