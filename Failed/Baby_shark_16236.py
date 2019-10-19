import collections
import sys
sys.stdin = open("sample_input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
theMap = []
for x in range(N):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        shark = [x, tmp.index(9), 0]
    theMap.append(tmp)

shark_size = 2
eaten = 0
is_update = True
while is_update:
    is_update = False
    deq = collections.deque()
    visited = collections.defaultdict(lambda: False)
    visited[(shark[0], shark[1])] = True
    deq.append(shark)

    candi = [20, 20, -1]
    while deq:
        cur = deq.popleft()

        if candi[2] != -1 and candi[2] < cur[2]:
            break

        if theMap[cur[0]][cur[1]] < shark_size and theMap[cur[0]][cur[1]] != 0:
            is_update = True
            if candi[0] > cur[0] or (candi[0] == cur[0] and candi[1] > cur[1]):
                candi = cur

        for dir in range(4):
            next = [cur[0] + dx[dir], cur[1] + dy[dir], cur[2] + 1]
            if next[0] >= 0 and next[0] < N and next[1] >= 0 and next[1] < N:
                if not visited[(next[0], next[1])] and shark_size >= theMap[next[0]][next[1]]:
                    visited[(next[0], next[1])] = True
                    deq.append(next)
    if is_update:
        theMap[shark[0]][shark[1]] = 0
        shark = candi
        eaten += 1
        if eaten == shark_size:
            shark_size += 1
            eaten = 0
        theMap[shark[0]][shark[1]] = 0
print(shark[2])