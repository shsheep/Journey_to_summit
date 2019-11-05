import collections

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate(fx: int, fy: int, mx: int, my: int, way: int, theMap: list):
    N = len(theMap)
    if way == 0 or way == 1:
        if fx != mx or fy > my:
            return False, None, None
        if way == 0:
            if fx+1 >= N or theMap[mx+1][my] == 1 or theMap[fx+1][fy] == 1:
                return False, None, None
            return True, fx+1, fy
        else:
            if fx-1 < 0 or theMap[mx-1][my] == 1 or theMap[fx-1][fy] == 1:
                return False, None, None
            return True, fx-1, fy
    elif way == 2 or way == 3:
        if fy != my or fx > mx:
            return False, None, None
        if way == 2:
            if fy-1 < 0 or theMap[mx][my-1] == 1 or theMap[fx][fy-1] == 1:
                return False, None, None
            return True, fx, fy-1
        else:
            if fy+1 >= N or theMap[mx][my+1] == 1 or theMap[fx][fy+1] == 1:
                return False, None, None
            return True, fx, fy+1
    elif way == 4 or way == 5:
        if fx != mx or fy < my:
            return False, None, None
        if way == 4:
            if fx-1 < 0 or theMap[fx-1][fy] == 1 or theMap[mx-1][my] == 1:
                return False, None, None
            return True, fx-1, fy
        else:
            if fx+1 >= N or theMap[fx+1][fy] == 1 or theMap[mx+1][my] == 1:
                return False, None, None
            return True, fx+1, fy
    elif way == 6 or way == 7:
        if fy != my or fx < mx:
            return False, None, None
        if way == 6:
            if fy+1 >= N or theMap[fx][fy+1] == 1 or theMap[mx][my+1] == 1:
                return False, None, None
            return True, fx, fy+1
        else:
            if fy-1 < 0 or theMap[fx][fy-1] == 1 or theMap[mx][my-1] == 1:
                return False, None, None
            return True, fx, fy-1


def bfs(theMap: list, rb: list):
    ret = 0xFFFF
    N = len(theMap)
    deq = collections.deque()
    visited = collections.defaultdict(lambda: False)
    start = (tuple(rb[0]), tuple(rb[1]), 0, 0)
    deq.append(start)
    visited[start] = True
    while deq:
        cur = deq.popleft()
        cnt = cur[2]
        if cnt >= ret:
            continue
        rot = cur[3]
        if (cur[0][0] == N-1 and cur[0][1] == N-1) or (cur[1][0] == N-1 and cur[1][1] == N-1):
            ret = min(ret, cnt)
            continue

        lx, ly = cur[0][0], cur[0][1]
        rx, ry = cur[1][0], cur[1][1]
        for dir in range(4):
            nlx, nly = lx + dx[dir], ly + dy[dir]
            nrx, nry = rx + dx[dir], ry + dy[dir]
            if nlx < 0 or nlx >= N or nly < 0 or nly >= N or nrx < 0 or nrx >= N or nry < 0 or nry >= N:
                continue
            if visited[((nlx, nly), (nrx, nry), cnt+1, rot)] or visited[((nrx, nry), (nlx, nly), cnt+1, rot)]:
                continue
            if theMap[nlx][nly] == 0 and theMap[nrx][nry] == 0:
                tmp = ((nlx, nly), (nrx, nry), cnt+1, rot)
                tmp2 = ((nrx, nry), (nlx, nly), cnt+1, rot)
                visited[tmp] = True
                visited[tmp2] = True
                deq.append(tmp)

        if rot % 2 == 0:
            rotation_list = [0, 1, 4, 5]
        else:
            rotation_list = [2, 3, 6, 7]
        for fix in range(2):
            fx, fy = cur[fix][0], cur[fix][1]
            mx, my = cur[(fix+1) % 2][0], cur[(fix+1) % 2][1]
            for how in rotation_list:
                possible, nx, ny = rotate(fx, fy, mx, my, how, theMap)
                if not possible:
                    continue
                if visited[((fx, fy), (nx, ny), cnt+1, rot+1)] or visited[((nx, ny), (fx, fy), cnt+1, rot+1)]:
                    continue
                if nx < fx or ny < fy:
                    tmp = ((nx, ny), (fx, fy), cnt+1, rot+1)
                else:
                    tmp = ((fx, fy), (nx, ny), cnt+1, rot+1)
                visited[((fx, fy), (nx, ny), cnt+1, rot+1)] = True
                visited[((nx, ny), (fx, fy), cnt+1, rot+1)] = True
                deq.append(tmp)

    return ret


def solution(board):
    robot = [[0, 0], [0, 1]]
    answer = bfs(board, robot)
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))