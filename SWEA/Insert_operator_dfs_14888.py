import sys

sys.stdin = open("sample_input.txt", "r")

def c14div(one: int, two: int):
    if one < 0:
        return (abs(one) // two) * -1
    else:
        return one // two

def dfs(result: int, cnt: int, idx: int):
    global max_val, min_val
    if cnt == N-1:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    for i in range(4):
        if opr[i] != 0:
            opr[i] -= 1
        else:
            continue
        if i == 0:
            dfs(result + A[idx], cnt + 1, idx + 1)
        elif i == 1:
            dfs(result - A[idx], cnt + 1, idx + 1)
        elif i == 2:
            dfs(result * A[idx], cnt + 1, idx + 1)
        else:
            dfs(c14div(result, A[idx]), cnt + 1, idx + 1)
        opr[i] += 1

N = int(input())
A = list(map(int, input().split()))
opr = list(map(int, input().split()))

max_val, min_val = -1000000000, 1000000000
dfs(A[0], 0, 1)
print(max_val)
print(min_val)
