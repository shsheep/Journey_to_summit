import collections

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a: int, b: int, ally: list):
    deq = collections.deque()
    deq.append(10 * a + b)
    visited[10 * a + b] = True
    tmp = []
    while deq:
        cur = deq.popleft()
        tmp.append(cur)
        for dir in range(4):
            nx, ny = (cur // 10) + dx[dir], (cur % 10) + dy[dir]
            if 0 <= nx and nx < N and 0 <= ny and ny < N and not visited[10 * nx + ny]:
                delta = abs(theMap[cur // 10][cur % 10] - theMap[nx][ny])
                if L <= delta and delta <= R:
                    deq.append(10 * nx + ny)
                    visited[10 * nx + ny] = True
    ally.append(tmp)

N, L, R = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))

ret = 0
while True:
    allies = []
    visited = collections.defaultdict(lambda: False)
    for x in range(N):
        for y in range(N):
            if not visited[10 * x + y]:
                bfs(x, y, allies)
    if len(allies) == N * N:
        break
    for u in allies:
        if len(u) == 0:
            continue
        total = 0
        for idx in u:
            total += theMap[idx // 10][idx % 10]
        for idx in u:
            theMap[idx // 10][idx % 10] = total // len(u)
    ret += 1

print(ret)