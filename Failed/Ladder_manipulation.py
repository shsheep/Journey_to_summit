import sys
sys.stdin = open("sample_input.txt", "r")

def check():
    for i in range(ladder_number):
        pos = i
        for j in range(possible_hor):
            if candidates[j][pos] == 1:
                pos += 1
            elif pos > 0 and candidates[j][pos-1] == 1:
                pos -= 1
        if pos != i:
            return False
    return True

def dfs(cnt: int, x: int, y: int):
    global ret
    if cnt >= ret:
        return
    if check():
        ret = min(ret, cnt)
        return
    elif cnt == 3:
        return

    for i in range(x, possible_hor):
        if i == x:
            k = y + 1
        else:
            k = 0
        for j in range(k, ladder_number - 1):
            if j == 0:
                if candidates[i][j] == 0 and candidates[i][j+1] == 0:
                    candidates[i][j] = 1
                    dfs(cnt + 1, i, j+1)
                    candidates[i][j] = 0
            elif j == ladder_number - 2:
                if candidates[i][j-1] == 0 and candidates[i][j] == 0:
                    candidates[i][j] = 1
                    dfs(cnt + 1, i, j+1)
                    candidates[i][j] = 0
            else:
                if candidates[i][j] == 0 and candidates[i][j-1] == 0 and candidates[i][j+1] == 0:
                    candidates[i][j] = 1
                    dfs(cnt + 1, i, j+1)
                    candidates[i][j] = 0

ladder_number, already_ladder, possible_hor = map(int, input().split())
candidates = []
for i in range(possible_hor):
    candidates.append([0] * ladder_number)
for i in range(already_ladder):
    a, b = map(int, input().split())
    candidates[a-1][b-1] = 1

ret = 4
dfs(0, 0, 0)
if ret == 4:
    ret = -1
print(ret)