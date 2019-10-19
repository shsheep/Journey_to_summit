import sys
import copy
sys.stdin = open("sample_input.txt", "r")

#게임같은 규칙을 구현하려면 디버깅에서 시간이 아주 오래 걸린다
#따라서, 큰 값만 구하면 되는 것이기 때문에
#한 방향의 이동만을 구현하고
#나머지 세 방향은 한 방향 이동 후 맵을 90도 회전시켜서 해결하라


def rotate(m: list):
    temp = []
    for _ in range(N):
        temp.append([0] * N)

    for x in range(N):
        for y in range(N):
            temp[x][y] = m[N - y - 1][x]

    for x in range(N):
        for y in range(N):
            m[x][y] = temp[x][y]

def get_max(m: list):
    maximum = 0
    for x in range(N):
        for y in range(N):
            if maximum < m[x][y]:
                maximum = m[x][y]
    return maximum

def up(m: list):
    temp = []
    for _ in range(N):
        temp.append([0] * N)

    for y in range(N):
        flag = 0
        target = -1
        for x in range(N):
            if m[x][y] == 0:
                continue
            if flag and m[x][y] == temp[target][y]:
                temp[target][y] *= 2
                flag = 0
            else:
                target += 1
                temp[target][y] = m[x][y]
                flag = 1
        for idx in range(target+1, N):
            temp[idx][y] = 0
    for x in range(N):
        for y in range(N):
            m[x][y] = temp[x][y]

def dfs(m: list, cnt: int):
    global ret
    if cnt == 5:
        candi = get_max(m)
        if ret < candi:
            ret = candi
        return

    for _ in range(4):
        next = copy.deepcopy(m)
        up(next)
        dfs(next, cnt+1)
        rotate(m)

N = int(input())
theMap = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    theMap.append(tmp)

ret = 0
dfs(theMap, 0)
print(ret)