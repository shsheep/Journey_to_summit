import collections
import sys
sys.stdin = open("sample_input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# def printMap(li: list):
#     for x in range(N):
#         for y in range(N):
#             print(li[x][y], end = ' ')
#         print()

def cpcp(dest: list, src: list):
    for x in range(N):
        for y in range(N):
            dest[x][y] = src[x][y]

def bfs(active_virus: list):
    global theMap
    visited = collections.defaultdict(lambda: False)
    deq = collections.deque()
    for vir in active_virus:
        deq.append((vir[0], vir[1], '0'))
        visited[(vir[0], vir[1])] = True

    # Make backup for original theMap
    backup = []
    for i in range(N):
        backup.append([0] * N)
    cpcp(backup, theMap)

    for i in range(N):
        for j in range(N):
            if theMap[i][j] == '1':
                theMap[i][j] = '-'
            elif theMap[i][j] == '2':
                theMap[i][j] = '*'

    max_time = 0
    while deq:
        cur = deq.popleft()
        for dir in range(4):
            nx, ny, nt = cur[0] + dx[dir], cur[1] + dy[dir], str(int(cur[2]) + 1)
            # If the new x and new y is in 0 ~ N,
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[(nx, ny)]:
                continue
            if theMap[nx][ny] != '-' and theMap[nx][ny] != '$' and theMap[nx][ny] != '*':
                theMap[nx][ny] = nt
                visited[(nx, ny)] = True
                deq.append((nx, ny, nt))
                if max_time < int(nt):
                    max_time = int(nt)

    # if the conditon is not accomplished, set the fail flag
    fail = False
    for x in range(N):
        for y in range(N):
            if theMap[x][y] == '0':
                fail = True
                break

    # For backtracking, copy the backup into theMap
    cpcp(theMap, backup)

    # printMap(theMap)
    if fail:
        return (N-1) * 2
    return max_time

# DFS for calculate combinations
def dfs(active_virus: list, start_idx):
    global ans
    # If the selected virus is met, do BFS
    if len(active_virus) == M:
        # print("This time viruses are ", active_virus)
        time = bfs(active_virus)
        if ans > time:
            ans = time
            # print("Answer is updated => ", time)
        return

    for idx in range(start_idx, len(virus)):
        x, y = virus[idx][0], virus[idx][1]
        if theMap[x][y] != '$':
            # Set for bfs
            theMap[x][y] = '$'
            active_virus.append((x, y))

            dfs(active_virus, idx+1)

            # Restoration for backtracking
            theMap[x][y] = '2'
            active_virus.pop()

N, M = map(int, input().split())
virus = []
theMap = []
for x in range(N):
    tmp = list(input().split())
    for y in range(N):
        if tmp[y] == '2':
            virus.append((x, y))
    theMap.append(tmp)
# print(virus)
ans = (N-1) * 2
dfs([], 0)
if ans == (N-1) * 2:
    ans = -1
print(ans)