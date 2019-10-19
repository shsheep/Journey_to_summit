import sys
import collections
import copy
sys.stdin = open("sample_input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global ret
    deq = collections.deque()
    visited = collections.defaultdict(lambda: False)
    backup = copy.deepcopy(theMap)

    for x in range(N):
        for y in range(M):
            if backup[x][y] == 2:
                deq.append(10 * x + y)
                visited[10 * x + y] = True

    while deq:
        cur = deq.popleft()
        nx = cur // 10
        ny = cur % 10

        for dir in range(4):
            kx = nx + dx[dir]
            ky = ny + dy[dir]
            if visited[10 * kx + ky]:
                continue
            if kx < 0 or ky < 0 or kx > N - 1 or ky > M - 1:
                continue
            if backup[kx][ky] == 0:
                backup[kx][ky] = 2
                visited[10 * kx + ky] = True
                deq.append(10 * kx + ky)

    candi = 0
    for x in range(N):
        for y in range(M):
            if backup[x][y] == 0:
                candi += 1
    ret = max(ret, candi)

def dfs(cnt: int, sx: int, sy: int):
    if cnt == 3:
        bfs()
        return

    for x in range(sx, N):
        for y in range(sy, M):
            if theMap[x][y] == 0:
                theMap[x][y] = 1
                dfs(cnt+1, x, y)
                theMap[x][y] = 0
        sy = 0

N, M = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))

ret = 0
dfs(0, 0, 0)
print(ret)