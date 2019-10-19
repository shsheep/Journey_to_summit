import sys
sys.stdin = open("sample_input.txt", "r")

def roll(dl: list, dir: int, new_num: int):
    if dir == 1:
        upper = dl[0][0]
        lower = dl[0][2] if new_num == 0 else new_num
        dl[0] = [dl[1][3]] + dl[0][0:2]
        dl[1] = [dl[1][0], upper, dl[1][2], lower]
    elif dir == 2:
        upper = dl[0][2]
        lower = dl[0][0] if new_num == 0 else new_num
        dl[0] = dl[0][1:] + [dl[1][3]]
        dl[1] = [dl[1][0], upper, dl[1][2], lower]

    elif dir == 3:
        upper = dl[1][2]
        lower = dl[1][0] if new_num == 0 else new_num
        dl[0] = [dl[0][0], upper, dl[0][2]]
        dl[1] = dl[1][1:] + [lower]
    else:
        upper = dl[1][0]
        lower = dl[1][2] if new_num == 0 else new_num
        dl[0] = [dl[0][0], upper, dl[0][2]]
        dl[1] = [dl[1][3]] + [dl[1][0], dl[1][1], lower]
    return upper, lower

N, M, x, y, num_comm = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))
comm = list(map(int, input().split()))

dice_line = [[0,0,0], [0,0,0,0]]
upper = lower = 0
for c in comm:
    if (c == 3 and x == 0) or (c == 2 and y == 0) or (c == 1 and y == M-1) \
        or (c == 4 and x == N-1):
        continue
    if c == 1:
        y += 1
    elif c == 2:
        y -= 1
    elif c == 3:
        x -= 1
    else:
        x += 1
    upper, lower = roll(dice_line, c, theMap[x][y])
    theMap[x][y] = lower if theMap[x][y] == 0 else 0
    print(upper)