import sys
sys.stdin = open("sample_input.txt", "r")

global n, m, h, ret
global ladders

def check():
    for i in range(n):
        pos = i
        for j in range(h):
            if ladders[j][pos] == 1:
                pos += 1
            elif pos > 0 and ladders[j][pos-1] == 1:
                pos -= 1
        if pos != i:
            return False
    return True

def dfs(cnt: int, y: int, x: int):
    global ret
    if cnt >= ret:
        return
    if check():
        ret = cnt
        return
    if cnt == 3:
        return
    for i in range(y, h):
        if i == y:
            k = y
        else:
            k = 0
        for j in range(k, n-1):
            if ladders[i][j] == 0 and ladders[i][j-1] == 0 and ladders[i][j+1] == 0:
                ladders[i][j] = 1
                dfs(cnt+1, i, j)
                ladders[i][j] = 0

n, m, h = map(int, input().split())
ladders = []
for i in range(h):
    ladders.append([0] * n)
for i in range(m):
    a, b = map(int, input().split())
    ladders[a-1][b-1] = 1
ret = 4
dfs(0, 1, 1)
if ret == 4:
    ret = -1
print(ret)