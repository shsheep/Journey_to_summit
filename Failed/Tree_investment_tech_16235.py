import collections
import sys
sys.stdin = open("sample_input.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def sprummer():
    global tree
    dummy = collections.deque()
    dead = []
    for t in tree:
        x, y, age = t
        if theMap[x][y] < age:
            dead.append(t)
            continue
        theMap[x][y] -= age
        t[2] += 1
        dummy.append(t)
    tree = dummy
    for tup in dead:
        x, y, age = tup
        theMap[x][y] += age // 2

def fall():
    global tree
    tmp = collections.deque()
    for tdx in range(len(tree) - 1, -1, -1):
        x, y, age = tree[tdx]
        if age < 5:
            break
        elif age % 5 == 0:
            for dir in range(8):
                nx, ny = x + dx[dir], y + dy[dir]
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    tmp.appendleft([nx, ny, 1])
    tree = tmp + tree

def winter():
    for x in range(N):
        for y in range(N):
            theMap[x][y] += nutri[x][y]

N, M, K = map(int, input().split())
theMap = []
nutri = []
tree_list = []
for _ in range(N):
    theMap.append([5] * N)
    nutri.append(list(map(int, input().split())))
for _ in range(M):
    tmp = list(map(int, input().split()))
    tree_list.append([tmp[0]-1, tmp[1]-1, tmp[2]])
tree_list.sort(key=lambda t: t[2])
tree = collections.deque()
for tl in tree_list:
    tree.append(tl)

for year in range(K):
    sprummer()
    fall()
    winter()
print(len(tree))