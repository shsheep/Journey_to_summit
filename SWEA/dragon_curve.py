import sys
sys.stdin = open("sample_input.txt", "r")

N = int(input())
spots = []
for _ in range(N):
    spots.append(list(map(int, input().split())))

grid = []
for i in range(101):
    grid.append([0] * 101)

dirs = []
for i in range(4):
    dirs.append([-1] * 11)
dirs[0][0], dirs[1][0], dirs[2][0], dirs[3][0] = [0], [1], [2], [3]
for dir in range(4):
    for gen in range(1, 11):
        tmp = dirs[dir][gen-1]
        to_append = []
        for idx in range(len(tmp)-1, -1, -1):
            to_append.append((tmp[idx] + 1) % 4)
        dirs[dir][gen] = tmp + to_append

dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)
for sp in spots:
    x, y = sp[0], sp[1]
    direction = sp[2]
    gen = sp[3]
    grid[x][y] = 1
    for move in dirs[direction][gen]:
        x, y = x + dx[move], y + dy[move]
        grid[x][y] = 1

ret = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1] :
            ret += 1
print(ret)
