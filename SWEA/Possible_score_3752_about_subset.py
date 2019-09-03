import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for case in range(1, T+1):
    N = int(input())
    problems = list(map(int, input().split()))
    problems.sort()
    visited = [0]
    every_case = [0 for _ in range(sum(problems) + 1)]
    every_case[0] = 1
    for score in problems:
        tmp = visited.copy()
        for v in tmp:
            if not every_case[score+v]:
                every_case[score+v] = 1
                visited.append(score+v)
    ret = sum(every_case)
    print("#{0} {1}".format(case, ret))