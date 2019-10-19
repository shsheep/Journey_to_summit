import sys

sys.stdin = open("sample_input.txt", "r")

def check():
    global ret
    red, blue = [], []
    for i in range(N):
        if picked[i] == 1:
            red.append(i)
        else:
            blue.append(i)

    red_score = blue_score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            red_score += S[red[i]][red[j]] + S[red[j]][red[i]]
            blue_score += S[blue[i]][blue[j]] + S[blue[j]][blue[i]]
    ret = min(ret, abs(red_score - blue_score))

def dfs(cnt: int, current: int):
    if cnt == N // 2:
        check()
        return
    for i in range(current, N):
        picked[i] = 1
        dfs(cnt + 1, i + 1)
        picked[i] = 0

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
red, blue = [], []
picked = [ 0 for _ in range(N)]

ret = 0xFFFF
dfs(0, 0)
print(ret)


'''
from itertools import combinations

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
answer = 0xffffff
member = set(range(n))
for c in combinations(range(n), n//2):
    temp = 0
    for x, y in combinations(c, 2):
        temp += a[x][y] + a[y][x]
    for x, y in combinations(member - set(c), 2):
        temp -= a[x][y] + a[y][x]
    answer = min(answer, abs(temp))
    if answer == 0:
        break
print(answer)
'''