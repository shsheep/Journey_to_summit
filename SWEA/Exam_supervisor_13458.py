import sys
import math

sys.stdin = open("sample_input.txt", "r")

ret = 0
N = int(input())
applicant = list(map(int, input().split()))
B, C = map(int, input().split())

for idx in range(N):
    applicant[idx] -= B
    ret += 1
for idx in range(N):
    if applicant[idx] > 0:
        num = int(math.ceil(applicant[idx] / C))
        ret += num
print(ret)