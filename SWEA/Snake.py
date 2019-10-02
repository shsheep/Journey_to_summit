import sys
sys.stdin = open("sample_input.txt", "r")
import collections

N = int(input())
K = int(input())

apples = dict()
for _ in range(K):
    tmp = list(map(int, input().split()))
    print('tmp is ', tmp)
    if tmp[0] - 1 not in apples:
        apples[tmp[0]-1] = [tmp[1]-1]
    else:
        apples[tmp[0]-1].append(tmp[1]-1)

print('apples is ', apples)

L = int(input())
x, y = 0, 0
turn = []
for _ in range(L):
    turn.append(tuple(input().split()))
print('each turn is ', turn)

snake_body = collections.deque()
snake_body.append((x, y))
turn_idx = 0
progress, dir = 0, 0
while True:
    if turn_idx < len(turn) and progress == int(turn[turn_idx][0]):
        if turn[turn_idx][1] == 'L':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        turn_idx += 1
    if dir == 0:
        y = y + 1
    elif dir == 1:
        x = x - 1
    elif dir == 2:
        y = y - 1
    else:
        x = x + 1
    progress += 1
    if x >= N or x < 0 or y >= N or y < 0 or (x, y) in snake_body:
        break
    if x in apples and y in apples[x]:
        snake_body.append((x, y))
        idx = apples[x].index(y)
        apples[x][idx] = -1
    else:
        snake_body.append((x, y))
        snake_body.popleft()
    print(x, y)
print(apples)
print(progress)