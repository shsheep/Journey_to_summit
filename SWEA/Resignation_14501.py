import sys
sys.stdin = open("sample_input.txt", "r")

memo = []

def dp(day: int):
    if day > N:
        return -1 * 0xFFFF
    if day == N:
        return 0
    if memo[day] != -1:
        return memo[day]

    memo[day] = max(dp(day+1), dp(day + T[day]) + P[day])

    return memo[day]

N = int(input())
tmp = []
for _ in range(N):
    tmp.append(tuple(map(int, input().split())))
T = [t for t, _ in tmp]
P = [p for _, p in tmp]

memo = [-1] * N
print(dp(0))