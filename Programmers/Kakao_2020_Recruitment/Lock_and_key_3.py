def rotate(li: list):
    ret = [[0] * len(li) for _ in range(len(li))]
    for x in range(len(li)):
        for y in range(len(li)):
            ret[x][y] = li[len(li)-y-1][x]
    return ret

def check(x: int, y: int, theMap: list, key: list):
    N, M = len(theMap) // 3, len(key)
    tmp = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            tmp[i][j] = theMap[x+i][y+j]
            theMap[x+i][y+j] += key[i][j]
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            if theMap[i][j] == 0 or theMap[i][j] == 2:
                for k in range(M):
                    for m in range(M):
                        theMap[x + k][y + m] = tmp[k][m]
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    theMap = [[0]* (3*N) for _ in range(3*N)]
    for x in range(N, 2*N):
        for y in range(N, 2*N):
            theMap[x][y] = lock[x%N][y%N]
    for turn in range(4):
        for x in range(N-M+1, 2*N):
            for y in range(N-M+1, 2*N):
                if check(x, y, theMap, key):
                    return True
        key = rotate(key)
    return False

print(solution([[1, 1, 1], [1, 1, 1], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))