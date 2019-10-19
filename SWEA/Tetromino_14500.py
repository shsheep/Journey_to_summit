import sys

def tetsum(theMap: list, x: int, y: int):
    max_t1 = max_t2 = 0
    t3 = []
    t4 = []
    t5 = []
    #tet1
    if y < len(theMap[0]) - 3:
        max_t1 = sum(theMap[x][y:y+4])
    if x < len(theMap) - 3:
        max_t1 = max(max_t1, theMap[x][y] + theMap[x+1][y] + theMap[x+2][y] + theMap[x+3][y])

    #tet2
    if y < len(theMap[0]) - 1 and x < len(theMap) - 1:
        max_t2 = theMap[x][y] + theMap[x][y+1] + theMap[x+1][y] + theMap[x+1][y+1]

    #tet3, 4, 5
    # 3 x 2
    if y < len(theMap[0]) - 2 and x < len(theMap) - 1:
        t3_1 = theMap[x+1][y] + theMap[x+1][y+1] + theMap[x+1][y+2] + theMap[x][y+2]
        t3_2 = theMap[x][y] + theMap[x+1][y] + theMap[x+1][y+1] + theMap[x+1][y+2]
        t3_3 = theMap[x][y] + theMap[x][y+1] + theMap[x][y+2] + theMap[x+1][y+2]
        t3_4 = theMap[x+1][y] + theMap[x][y] + theMap[x][y+1] + theMap[x][y+2]
        t3 = [t3_1, t3_2, t3_3, t3_4]

        t4_1 = theMap[x+1][y] + theMap[x+1][y+1] + theMap[x][y+1] + theMap[x][y+2]
        t4_2 = theMap[x][y] + theMap[x][y+1] + theMap[x+1][y+1] + theMap[x+1][y+2]
        t4 = [t4_1, t4_2]

        t5_1 = theMap[x][y] + theMap[x][y+1] + theMap[x][y+2] + theMap[x+1][y+1]
        t5_2 = theMap[x+1][y] + theMap[x+1][y+1] + theMap[x+1][y+2] + theMap[x][y+1]
        t5 = [t5_1, t5_2]
    # 2 x 3
    if y < len(theMap[0]) - 1 and x < len(theMap) - 2:
        t3_5 = theMap[x][y] + theMap[x+1][y] + theMap[x+2][y] + theMap[x+2][y+1]
        t3_6 = theMap[x][y+1] + theMap[x+1][y+1] + theMap[x+2][y+1] + theMap[x+2][y]
        t3_7 = theMap[x][y] + theMap[x+1][y] + theMap[x+2][y] + theMap[x][y+1]
        t3_8 = theMap[x][y] + theMap[x+1][y+1] + theMap[x+2][y+1] + theMap[x][y+1]
        t3 += [t3_5, t3_6, t3_7, t3_8]

        t4_3 = theMap[x][y] + theMap[x+1][y] + theMap[x+1][y+1] + theMap[x+2][y+1]
        t4_4 = theMap[x][y+1] + theMap[x+1][y+1] + theMap[x+1][y] + theMap[x+2][y]
        t4 += [t4_3, t4_4]

        t5_3 = theMap[x][y+1] + theMap[x+1][y+1] + theMap[x+2][y+1] + theMap[x+1][y]
        t5_4 = theMap[x][y] + theMap[x+1][y] + theMap[x+2][y] + theMap[x+1][y+1]
        t5 += [t5_3, t5_4]
    if t3 and t4 and t5:
        max_t3, max_t4, max_t5 = max(t3), max(t4), max(t5)
        return max(max_t1, max(max_t2, max(max_t3, max(max_t4, max_t5))))
    else:
        return max(max_t1, max_t2)

sys.stdin = open("sample_input.txt", "r")

N, M = map(int, input().split())
theMap = []
for _ in range(N):
    theMap.append(list(map(int, input().split())))

ret = 0
for x in range(N):
    for y in range(M):
        ret = max(ret, tetsum(theMap, x, y))
print(ret)