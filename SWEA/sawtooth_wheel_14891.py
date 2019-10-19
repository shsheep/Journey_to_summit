import sys

sys.stdin = open("sample_input.txt", "r")

def turn(wheel: str, dir: int):
    if dir == 1:
        return wheel[-1:] + wheel[0:-1]
    else:
        return wheel[1:] + wheel[0:1]

whs = []
for _ in range(4):
    whs.append(input())
N = int(input())
rotate = []
for _ in range(N):
    rotate.append(list(map(int, input().split())))
rotate = [[num - 1, dir] for num, dir in rotate]

for r in rotate:
    if r[0] == 0:
        if whs[0][2] != whs[1][6]:
            if whs[1][2] != whs[2][6]:
                if whs[2][2] != whs[3][6]:
                    whs[3] = turn(whs[3], -1 * r[1])
                whs[2] = turn(whs[2], r[1])
            whs[1] = turn(whs[1], -1 * r[1])
        whs[0] = turn(whs[0], r[1])

    elif r[0] == 1:
        if whs[0][2] != whs[1][6] and whs[1][2] != whs[2][6]:
            if whs[2][2] != whs[3][6]:
                whs[3] = turn(whs[3], r[1])
            whs[0] = turn(whs[0], -1 * r[1])
            whs[2] = turn(whs[2], -1 * r[1])
        elif whs[0][2] != whs[1][6] and whs[1][2] == whs[2][6]:
            whs[0] = turn(whs[0], -1 * r[1])
        elif whs[0][2] == whs[1][6] and whs[1][2] != whs[2][6]:
            if whs[2][2] != whs[3][6]:
                whs[3] = turn(whs[3], r[1])
            whs[2] = turn(whs[2], -1 * r[1])
        whs[1] = turn(whs[1], r[1])

    elif r[0] == 2:
        if whs[1][2] != whs[2][6] and whs[2][2] != whs[3][6]:
            if whs[0][2] != whs[1][6]:
                whs[0] = turn(whs[0], r[1])
            whs[1] = turn(whs[1], -1 * r[1])
            whs[3] = turn(whs[3], -1 * r[1])
        elif whs[2][2] != whs[3][6] and whs[1][2] == whs[2][6]:
            whs[3] = turn(whs[3], -1 * r[1])
        elif whs[2][2] == whs[3][6] and whs[1][2] != whs[2][6]:
            if whs[0][2] != whs[1][6]:
                whs[0] = turn(whs[0], r[1])
            whs[1] = turn(whs[1], -1 * r[1])
        whs[2] = turn(whs[2], r[1])

    else:
        if whs[2][2] != whs[3][6]:
            if whs[1][2] != whs[2][6]:
                if whs[0][2] != whs[1][6]:
                    whs[0] = turn(whs[0], -1 * r[1])
                whs[1] = turn(whs[1], r[1])
            whs[2] = turn(whs[2], -1 * r[1])
        whs[3] = turn(whs[3], r[1])

ret = 0
if whs[0][0] == '1':
    ret += 1
if whs[1][0] == '1':
    ret += 2
if whs[2][0] == '1':
    ret += 4
if whs[3][0] == '1':
    ret += 8
print(ret)