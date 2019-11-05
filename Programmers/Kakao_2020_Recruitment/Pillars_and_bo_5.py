def cpcp(dest: list, src: list):
    for x in range(len(src)):
        for y in range(len(src)):
            dest[x][y] = src[x][y]

def pil_bot(num: int):
    return num // 1000

def pil_top(num: int):
    return (num // 100) % 10

def bo_start(num: int):
    return (num // 10) % 10

def bo_end(num: int):
    return num % 10
#
#
# 10   10 1 11
# 21 1 12 2 21
# 10        10
# [[0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [4, 0, 0, 1], [4, 1, 0, 1], [3, 1, 1, 1], [3, 2, 1, 1], [2, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 0, 0, 0], [2, 1, 1, 1]]
def is_wrong(li: list):
    for x in range(len(li)-1):
        for y in range(len(li)-1):
            # Pillar
            if x != 0 and pil_bot(li[x][y]) and not pil_top(li[x][y]) and not (bo_start(li[x][y]) \
                    or bo_end(li[x][y])):
                print("Pillar Problem ", x, y)
                return True

            # Bo
            if bo_start(li[x][y]) and not pil_top(li[x][y]) and not pil_top(li[x][y+1]):
                if not bo_start(li[x][y+1]):
                    print("Bo Problem_1 -_ ", x, y)
                    return True
                elif not bo_end(li[x][y]):
                    print("Bo Problem_2 _- ", x, y)
                    return True

    return False


def solution(n, build_frame):
    answer = []
    theMap = [[0] * (n+1) for _ in range(n+1)]
    for bf in build_frame:
        backup = [ [0] * (n+1) for _ in range(n+1)]
        # print(theMap, backup)
        cpcp(backup, theMap)
        x, y = bf[1], bf[0]
        if bf[3] == 1:
            if bf[2] == 0:
                theMap[x][y] += 1000
                theMap[x+1][y] += 100
            else:
                theMap[x][y] += 10
                theMap[x][y+1] += 1
        else:
            if bf[2] == 0:
                theMap[x][y] -= 1000
                theMap[x+1][y] -= 100
            else:
                theMap[x][y] -= 10
                theMap[x][y+1] -= 1
        if is_wrong(theMap):
            print("impossible ", bf)
            cpcp(theMap, backup)
    print("Constructed")
    for line in theMap:
        print(line)
    for y in range(n+1):
        for x in range(n+1):
            if x != n and pil_bot(theMap[x][y]):
                answer.append([y, x, 0])
                theMap[x][y] -= 1000
                theMap[x+1][y] -= 100
            if y != n and bo_start(theMap[x][y]):
                answer.append([y, x, 1])
                theMap[x][y] -= 10
                theMap[x][y+1] -= 1
    print("Deconstructed")
    for line in theMap:
        print(line)
    # answer.sort(key = lambda li: li[0])
    return answer
# 10      1 11    10      1  1
# 21 2  2 2 21    21 2 2  2 11
# 10        10    10        10
# [[0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [4, 0, 0, 1], [4, 1, 0, 1], [3, 1, 1, 1], [3, 2, 1, 1], [2, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 0, 0, 0], [2, 1, 1, 1]]
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
print(solution(5, [[0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [4, 0, 0, 1], [4, 1, 0, 1], [3, 1, 1, 1], [3, 2, 1, 1], [2, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 0, 0, 0], [2, 1, 1, 1], \
                   [2, 1, 0, 0], [2, 1, 1, 0], [3, 1, 1, 0], [4, 1, 0, 0]]))