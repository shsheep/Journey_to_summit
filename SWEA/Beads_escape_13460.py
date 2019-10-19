import sys
import collections

sys.stdin = open("sample_input.txt", "r")

def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = collections.defaultdict(lambda : 0)
    deq = collections.deque()
    deq.append(start)
    visited[tuple(start)] = 1
    ret = -1
    while deq:
        cur = deq.popleft()
        if cur[-1] > 10:
            break
        if theMap[cur[0]][cur[1]] == 'O' and theMap[cur[2]][cur[3]] != 'O':
            ret = cur[-1]
            break
        for dir in range(4):
            next_ry = cur[0]
            next_rx = cur[1]
            next_by = cur[2]
            next_bx = cur[3]

            while True:
                if theMap[next_ry][next_rx] != '#' and theMap[next_ry][next_rx] != 'O':
                    next_ry += dy[dir]
                    next_rx += dx[dir]
                else:
                    if theMap[next_ry][next_rx] == '#':
                        next_ry -= dy[dir]
                        next_rx -= dx[dir]
                    break
            while True:
                if theMap[next_by][next_bx] != '#' and theMap[next_by][next_bx] != 'O':
                    next_by += dy[dir]
                    next_bx += dx[dir]
                else:
                    if theMap[next_by][next_bx] == '#':
                        next_by -= dy[dir]
                        next_bx -= dx[dir]
                    break

            if next_ry == next_by and next_rx == next_bx:
                if theMap[next_ry][next_rx] != 'O':
                    red_dist = abs(next_ry - cur[0]) + abs(next_rx - cur[1])
                    blue_dist = abs(next_by - cur[2]) + abs(next_bx - cur[3])
                    if red_dist < blue_dist:
                        next_by -= dy[dir]
                        next_bx -= dx[dir]
                    else:
                        next_ry -= dy[dir]
                        next_rx -= dx[dir]

            if visited[tuple([next_ry, next_rx, next_by, next_bx, cur[-1] + 1])] == 0:
                visited[tuple([next_ry, next_rx, next_by, next_bx, cur[-1] + 1])] = 1
                next = [next_ry, next_rx, next_by, next_bx, cur[-1] + 1]
                deq.append(next)

    return ret

N, M = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(input())

start = [-1, -1, -1, -1, 0]
for i in range(N):
    for j in range(M):
        if theMap[i][j] == 'R':
            start[0], start[1] = i, j
        if theMap[i][j] == 'B':
            start[2], start[3] = i, j
ans = bfs()
print(ans)