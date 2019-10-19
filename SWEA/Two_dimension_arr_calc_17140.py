import collections
import sys
sys.stdin = open("sample_input.txt", "r")
'''
def solve():
    rsize = csize = 3
    for t in range(101):
        if arr[R][C] == K:
            return t
        if rsize >= csize:
            for i in range(rsize):
                nums = []
                cnter = [0] * 101
                for j in range(csize):
                    cnter[arr[i][j]] += 1
                for c in range(1, 101):
                    if cnter[c] > 0:
                        nums.append((c, cnter[c]))
                nums.sort(key = lambda tup: tup[1])
                idx = 0
                for tup in nums:
                    if idx >= 99:
                        break
                    arr[i][idx] = tup[0]
                    arr[i][idx+1] = tup[1]
                    idx += 2
                csize = max(csize, idx)
                for jdx in range(idx, 100):
                    arr[i][jdx] = 0
        else:
            for j in range(csize):
                nums = []
                cnter = [0] * 101
                for i in range(rsize):
                    cnter[arr[i][j]] += 1
                for c in range(1, 101):
                    if cnter[c] > 0:
                        nums.append((c, cnter[c]))
                nums.sort(key = lambda tup: tup[1])
                idx = 0
                for tup in nums:
                    if idx >= 99:
                        break
                    arr[idx][j] = tup[0]
                    arr[idx+1][j] = tup[1]
                    idx += 2
                rsize = max(rsize, idx)
                for jdx in range(idx, 100):
                    arr[jdx][j] = 0
    return -1

R, C, K = map(int, input().split())
R -= 1
C -= 1
arr = []
for _ in range(100):
    arr.append([0] * 100)

for i in range(3):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())
print(solve())
'''
'''
RUNTIME ERROR
def R_sort(mat: list, aux: bool):
    global max_row, max_col
    for idx, r in enumerate(mat):
        tmp = []
        cnter = collections.Counter(r)
        set_list = list(set(r))
        for num in set_list:
            if num != 0:
                tmp.append((num, cnter[num]))
        tmp.sort(key = lambda tup: tup[1])
        to_swap = []
        for tup in tmp:
            to_swap.append(tup[0])
            to_swap.append(tup[1])
        mat[idx] = to_swap
        if not aux and max_row < len(mat[idx]):
            max_col = len(mat[idx])
        elif aux and max_row < len(mat[idx]):
            max_row = len(mat[idx])
    if not aux:
        for idx, r in enumerate(mat):
            if len(mat[idx]) < max_col:
                mat[idx] += [0] * (max_col - len(mat[idx]))
    elif aux:
        for idx, r in enumerate(mat):
            if len(mat[idx]) < max_row:
                mat[idx] += [0] * (max_row - len(mat[idx]))

def C_sort(mat: list):
    rotate = []
    for _ in range(max_col):
        rotate.append([0] * max_row)
    for x in range(max_col):
        for y in range(max_row):
            rotate[x][y] = mat[y][x]
    R_sort(rotate, True)
    if len(mat) < max_row:
        for _ in range(max_row - len(mat)):
            mat.append([0] * max_col)

    for x in range(max_row):
        for y in range(max_col):
            mat[x][y] = rotate[y][x]

R, C, K = map(int, input().split())
R -= 1
C -= 1
mat = []
for _ in range(3):
    mat.append(list(map(int, input().split())))
max_row = max_col = 3

ans = 0
while mat[R][C] != K and ans < 100:
    if max_row >= max_col:
        R_sort(mat, False)
    else:
        C_sort(mat)
    max_row = min(100, max_row)
    max_col = min(100, max_col)
    ans += 1
if ans == 100:
    ans = -1
print(ans)
'''

def R_sort(mat: list):
    global max_row, max_col
    for idx in range(max_row):
        cnter = collections.Counter(mat[idx])
        set_list = list(set(mat[idx]))
        nums = []
        '''
        for jdx in range(max_col):
            cnter[mat[idx][jdx]] += 1
        for c in range(1, 101):
            if cnter[c] > 0:
                nums.append((c, cnter[c]))
        '''
        for num in set_list:
            if num != 0 and cnter[num] > 0:
                nums.append((num, cnter[num]))
        nums.sort(key = lambda tup: tup[1])
        kdx = 0
        for tup in nums:
            if kdx >= 99:
                break
            mat[idx][kdx], mat[idx][kdx+1] = tup[0], tup[1]
            kdx += 2
        max_col = max(max_col, kdx)
        for ldx in range(kdx, 100):
            mat[idx][ldx] = 0


def C_sort(mat: list):
    global max_row, max_col
    for jdx in range(max_col):
        cnter = [0] * 101
        nums = []
        for idx in range(max_row):
            cnter[mat[idx][jdx]] += 1
        for c in range(1, 101):
            if cnter[c] > 0:
                nums.append((c, cnter[c]))
        nums.sort(key = lambda tup: tup[1])
        kdx = 0
        for tup in nums:
            if kdx >= 99:
                break
            mat[kdx][jdx], mat[kdx + 1][jdx] = tup[0], tup[1]
            kdx += 2
        max_row = max(max_row, kdx)
        for ldx in range(kdx, 100):
            mat[ldx][jdx] = 0

R, C, K = map(int, input().split())
R -= 1
C -= 1
mat = []
for _ in range(100):
    mat.append([0] * 100)
max_row = max_col = 3
for i in range(3):
    mat[i][0], mat[i][1], mat[i][2] = map(int, input().split())

ans = 0
while mat[R][C] != K and ans < 101:
    if max_row >= max_col:
        R_sort(mat)
    else:
        C_sort(mat)
    ans += 1
if ans > 100:
    ans = -1
print(ans)