import sys
import itertools
import collections
sys.stdin = open("sample_input.txt", "r")

def bfs_connected(target: list, other: list, graph: list):
    visited = [False] * len(graph)
    for t in other:
        visited[t] = True
    deq = collections.deque()
    deq.append(target[0])
    while deq:
        cur = deq.popleft()
        visited[cur] = True
        for idx, connected in enumerate(graph[cur]):
            if connected and not visited[idx]:
                deq.append(idx)
    if False in visited:
        return False
    return True

def bfs(one: list, two:list, graph: list):
    temp_graph = []
    for g in graph:
        temp = g.copy()
        temp_graph.append(temp)
    for x in one:
        for y in two:
            if graph[x][y] != 0:
                temp_graph[x][y] = 0
    if not bfs_connected(one, two, temp_graph) or not bfs_connected(two, one, temp_graph):
        return False
    return True


N = int(input())
popul = list(map(int, input().split()))
neighbor = []
for _ in range(N):
    neighbor.append(list(map(int, input().split())))
for idx in range(N):
    neighbor[idx] = [elem - 1 for elem in neighbor[idx][1:]]
graph = [ [0] * N for _ in range(N)]
for idx, n in enumerate(neighbor):
    for elem in n:
        graph[idx][elem] = 1
for g in graph:
    print(g)

section = [i for i in range(N)]
print(section)

answer = 0xFFFF
for i in range(1, N // 2 + 1):
    for case in itertools.combinations(section, i):
        sec_1 = list(case)
        sec_2 = section.copy()
        for s in sec_1:
            sec_2.remove(s)
        print(sec_1, sec_2)
        if bfs(sec_1, sec_2, graph):
            sum_1 = 0
            for s in sec_1:
                sum_1 += popul[s]
            sum_2 = 0
            for s in sec_2:
                sum_2 += popul[s]
            answer = min(answer, abs(sum_1 - sum_2))
if answer == 0xFFFF:
    answer = -1
print(answer)