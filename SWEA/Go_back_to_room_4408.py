import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for case in range(1, T+1):
    N = int(input())
    students = []
    for _ in range(N):
        students.append(list(map(int, input().split())))
    for stu in students:
        if stu[0] > stu[1]:
            stu[0], stu[1] = stu[1], stu[0]
        stu[0] -= 1
        stu[1] -= 1
    students.sort()
    print(students)
    ret = 1
    for idx, st in enumerate(students):
        if idx == 0:
            start, end = st[0], st[1]
            continue
        if end < st[0] and (end // 2) != (st[0] // 2):
            start, end = st[0], st[1]
            # continue
        else:
            ret += 1
            start, end = st[0], st[1]
            # continue

        # else:
    print("#{0} {1}".format(case, ret))