import itertools
import collections
import sys

sys.stdin = open("sample_input.txt", "r")

# BFS for checking the connectivity among islands
def is_connected(graph: list):
    deq = collections.deque()
    visited = collections.defaultdict(lambda : False)

    deq.append(0)
    visited[0] = True

    while deq:
        cur = deq.popleft()
        for i in range(len(graph)):
            if graph[cur][i] == 1 and not visited[i]:
                deq.append(i)
                visited[i] = 1
    for i in range(n):
        if not visited[i]:
            return False
    return True

N, M = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))

ret = 0xFFFF
islands = []

for x in range(N):
    for y in range(M):
        if theMap[x][y] == 1:
            if len(islands) == 0:
                tmp = [10 * x + y]
                islands.append(tmp)
                continue
            if x == 0 and y - 1 >= 0:
                if theMap[x][y-1] == 1:
                    for idx, isl in enumerate(islands):
                        if 10*x + y - 1 in isl:
                            islands[idx].append(10 * x + y)
                            break
                    continue
                tmp = [10 * x + y]
                islands.append(tmp)

            elif y == 0 and x - 1 >= 0:
                if theMap[x-1][y] == 1:
                    for idx, isl in enumerate(islands):
                        if 10 * (x - 1) + y in isl:
                            islands[idx].append(10 * x + y)
                            break
                    continue
                tmp = [10 * x + y]
                islands.append(tmp)

            else:
                if theMap[x-1][y] == 1:
                    for idx, isl in enumerate(islands):
                        if 10 * (x - 1) + y in isl:
                            islands[idx].append(10 * x + y)
                            break
                    continue
                elif theMap[x][y-1] == 1:
                    for idx, isl in enumerate(islands):
                        if 10 * x + y - 1 in isl:
                            islands[idx].append(10 * x + y)
                            break
                    continue
                tmp = [10 * x + y]
                islands.append(tmp)


for i in islands:
    print(i)


bridges = []
for i in range(len(islands)):
    one = islands[i]
    for j in range(i+1, len(islands)):
        two = islands[j]
        candi_1, candi_2 = [], []
        ver, hor = False, False
        for o in one:
            for t in two:
                if o // 10 != t // 10 and o % 10 != t % 10:
                    continue
                # Horizontal bridges
                if o // 10 == t // 10:
                    candi_1.append(o)
                    candi_2.append(t)
                    hor = True
                # Vertical bridges
                elif o % 10 == t % 10:
                    candi_1.append(o)
                    candi_2.append(t)
                    ver = True
        if hor:
            if candi_1[-1] % 10 < candi_2[0] % 10:
                left = candi_1[-1]
                right = candi_2[0]
            else:
                left = candi_2[-1]
                right = candi_1[0]
            length = (right % 10) - (left % 10) - 1
            if length < 2:
                continue
            possible = True
            for y in range(left % 10 + 1, right % 10):
                if theMap[left // 10][y] == 1:
                    possible = False
                    break
            if not possible:
                continue
            to_append = [i, j, length, 'h', left // 10]
            bridges.append(to_append)

        elif ver:
            if candi_1[-1] // 10 < candi_2[0] // 10:
                left = candi_1[-1]
                right = candi_2[0]
            else:
                left = candi_2[-1]
                right = candi_1[0]
            length = (right // 10) - (left // 10) - 1
            if length < 2:
                continue
            possible = True
            for x in range(left // 10 + 1, right // 10):
                if theMap[x][left % 10] == 1:
                    possible = False
                    break
            if not possible:
                continue
            to_append = [i, j, length, 'v', left % 10]
            bridges.append(to_append)

print()
for b in bridges:
    print(b)
print()

ret = 0xFFFF
for n in range(len(islands) - 1, len(bridges)+1):
    for tup in itertools.combinations(bridges, n):
        print(tup)
        connected = []
        for _ in range(len(islands)):
            connected.append([0] * len(islands))
        dummy = 0
        for t in tup:
            connected[t[0]][t[1]] = 1
            connected[t[1]][t[0]] = 1
            dummy += t[2]
        if not is_connected(connected):
            print("not_connected")
            continue
        ret = min(ret, dummy)
if ret == 0xFFFF:
    ret = -1
print(ret)