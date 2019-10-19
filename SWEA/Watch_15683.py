import sys
sys.stdin = open("sample_input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 10, 11, 12, 13
# 20, 21
# 30, 31, 32, 33
# 40, 41, 42, 43
# 50

def shoot(dir: int, x: int, y: int, backup: list):
    nx, ny = x + dx[dir], y + dy[dir]
    while True:
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if backup[nx][ny] == 0:
            backup[nx][ny] = '#'
        elif backup[nx][ny] == 6:
            break
        nx += dx[dir]
        ny += dy[dir]

def spread(cctv: int, backup: list, loc: tuple):
    num = cctv // 10
    dir = cctv % 10
    x, y = loc[0], loc[1]
    if num == 1:
        shoot(dir, x, y, backup)
    elif num == 2:
        shoot(dir, x, y, backup)
        shoot((dir + 2) % 4, x, y, backup)
    elif num == 3:
        shoot(dir, x, y, backup)
        shoot((dir + 1) % 4, x, y, backup)
    elif num == 4:
        shoot(dir, x, y, backup)
        shoot((dir + 1) % 4, x, y, backup)
        shoot((dir + 2) % 4, x, y, backup)
    elif num == 5:
        shoot(dir, x, y, backup)
        shoot((dir + 1) % 4, x, y, backup)
        shoot((dir + 2) % 4, x, y, backup)
        shoot((dir + 3) % 4, x, y, backup)

def count_deadzone(m: list):
    dz = 0
    for row in m:
        for elem in row:
            if elem == 0:
                dz += 1
    return dz

def cpcp(dest: list, src: list):
    for x in range(N):
        for y in range(M):
            dest[x][y] = src[x][y]

def dfs(cnt: int, office: list):
    global ret, cctv
    tmp_map = []
    for _ in range(N):
        tmp_map.append( [0] * M)

    if cnt == len(cctv):
        ret = min(ret, count_deadzone(office))
        return
    cam = cctv[cnt][2]
    if cam == 1 or cam == 3 or cam == 4:
        for dir in range(4):
            '''
            WAY SLOWER!!!!
            tmp_map = copy.deepcopy(office)
            direction = cam * 10 + dir
            spread(direction, tmp_map, cctv[cnt])
            dfs(cnt + 1, tmp_map)
            '''
            cpcp(tmp_map, office)
            direction = cam * 10 + dir
            spread(direction, office, cctv[cnt])
            dfs(cnt + 1, office)
            cpcp(office, tmp_map)

    elif cam == 2:
        for dir in range(2):
            '''
            WAY SLOWER!!!!
            tmp_map = copy.deepcopy(office)
            direction = cam * 10 + dir
            spread(direction, tmp_map, cctv[cnt])
            dfs(cnt + 1, tmp_map)
            '''
            cpcp(tmp_map, office)
            direction = cam * 10 + dir
            spread(direction, office, cctv[cnt])
            dfs(cnt + 1, office)
            cpcp(office, tmp_map)

    else:
        '''
        WAY SLOWER!!!!
        tmp_map = copy.deepcopy(office)
        direction = cam * 10
        spread(direction, tmp_map, cctv[cnt])
        dfs(cnt + 1, tmp_map)
        '''
        cpcp(tmp_map, office)
        direction = cam * 10
        spread(direction, office, cctv[cnt])
        dfs(cnt + 1, office)
        cpcp(office, tmp_map)


N, M = map(int, input().split())
theMap = []
cctv = []
for x in range(N):
    tmp = list(map(int, input().split()))
    for y in range(M):
        if tmp[y] != 0 and tmp[y] != 6:
            cctv.append((x, y, tmp[y]))
    theMap.append(tmp)

ret = 65
dfs(0, theMap)
print(ret)