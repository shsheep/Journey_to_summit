import collections
import itertools
import sys

sys.stdin = open("sample_input.txt", "r")

N = int(input())
An = collections.deque(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
opr = ['+'] * add + ['-'] * sub + ['*'] * mul +['/'] * div
visited = collections.defaultdict(lambda: False)

max_val, min_val = -1000000000, 1000000000
for case in itertools.permutations(opr, N-1):
    if visited[case]:
        continue
    visited[case] = True
    A = An.copy()
    for op in case:
        num_1 = A.popleft()
        num_2 = A.popleft()
        if op == '+':
            result = num_1 + num_2
        elif op == '-':
            result = num_1 - num_2
        elif op == '*':
            result = num_1 * num_2
        else:
            result = abs(num_1) // num_2
            if num_1 < 0:
                result *= -1
        A.appendleft(result)

    max_val = max(max_val, A[0])
    min_val = min(min_val, A[0])
print(max_val)
print(min_val)
