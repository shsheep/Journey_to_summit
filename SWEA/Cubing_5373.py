import sys

sys.stdin = open("sample_input.txt", "r")

def make_upper(ver1: list, ver2: list, ver3: list, hor1: list, hor2: list, hor3: list):
    global upper
    upper = [[ver1[0], ver2[0], ver3[0]], [ver1[1], ver2[1], ver3[1]], [ver1[2], ver2[2], ver3[2]]]

def make_lower(ver1: list, ver2: list, ver3: list, hor1: list, hor2: list, hor3: list):
    global lower
    lower = [[ver1[6], ver2[6], ver3[6]], [ver1[7], ver2[7], ver3[7]], [ver1[8], ver2[8], ver3[8]]]

def make_front(ver1: list, ver2: list, ver3: list, hor1: list, hor2: list, hor3: list):
    global front
    #front = [[ver1[3], ver2[3], ver3[3]], [ver1[4], ver2[4], ver3[4]], [ver1[5], ver2[5], ver3[5]]]
    front = [[hor1[3], hor1[4], hor1[5]], [hor2[3], hor2[4], hor2[5]], [hor3[3], hor3[4], hor3[5]]]

def make_behind(ver1: list, ver2: list, ver3: list, hor1: list, hor2: list, hor3: list):
    global behind
    behind = [[ver1[9], ver2[9], ver3[9]], [ver1[10], ver2[10], ver3[10]], [ver1[11], ver2[11], ver3[11]]]

def make_left(ver1: list, ver2: list, ver3: list, hor1: list, hor2: list, hor3: list):
    global left
    left = [[hor1[0], hor1[1], hor1[2]], [hor2[0], hor2[1], hor2[2]], [hor3[0], hor3[1], hor3[2]]]

def make_right(ver1: list, ver2: list, ver3: list, hor1: list, hor2: list, hor3: list):
    global right
    right = [[hor1[-3], hor1[-2], hor1[-1]], [hor2[-3], hor2[-2], hor2[-1]], [hor3[-3], hor3[-2], hor3[-1]]]

def cpcp(dest: list, src: list):
    for i in range(3):
        for j in range(3):
            dest[i][j] = src[i][j]

def cp_part(dest_1: list, dest_2: list, dest_3: list, src_1: list, src_2: list, src_3: list):
    dest_1[3], dest_1[4], dest_1[5] = src_1[3], src_2[3], src_3[3]
    dest_2[3], dest_2[4], dest_2[5] = src_1[4], src_2[4], src_3[4]
    dest_3[3], dest_3[4], dest_3[5] = src_1[5], src_2[5], src_3[5]

def bingle(rot: str):
    global upper, lower, front, behind, left, right, ver_3, ver_2, ver_1, hor_3, hor_2, hor_1
    dummy = []
    for _ in range(3):
        dummy.append([0] * 3)

    if rot[0] == 'U':
        if rot[1] == '+':
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = upper[3-y-1][x]
            cpcp(upper, dummy)
            a, b, c = hor_1[0], hor_1[1], hor_1[2]
            hor_1 = hor_1[3:] + ver_3[-1:] + ver_2[-1:] + ver_1[-1:]
            ver_1[-1], ver_2[-1], ver_3[-1] = a, b, c
        else:
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = upper[y][3-x-1]
            cpcp(upper, dummy)
            a, b, c = hor_1[-3], hor_1[-2], hor_1[-1]
            hor_1 = ver_3[-1:] + ver_2[-1:] + ver_1[-1:] + hor_1[:6]
            ver_3[-1], ver_2[-1], ver_1[-1] = a, b, c
        cp_part(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)

    elif rot[0] == 'D':
        if rot[1] == '+':
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = lower[3-y-1][x]
            cpcp(lower, dummy)
            a, b, c = hor_3[-3], hor_3[-2], hor_3[-1]
            hor_3 =  ver_3[-3:-2] + ver_2[-3:-2] + ver_1[-3:-2] + hor_3[3:]
            ver_3[-3], ver_2[-3], ver_1[-3] = a, b, c
        else:
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = lower[y][3-x-1]
            cpcp(lower, dummy)
            a, b, c = hor_3[0], hor_3[1], hor_3[2]
            hor_3 =  hor_3[3:] + ver_3[-3:-2] + ver_2[-3:-2] + ver_1[-3:-2]
            ver_3[-3], ver_2[-3], ver_1[-3] = a, b, c
        cp_part(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)

    elif rot[0] == 'F':
        if rot[1] == '+':
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = front[3-y-1][x]
            cpcp(front, dummy)
            a, b, c = ver_1[2], ver_2[2], ver_3[2]
            ver_1[2] = hor_3[2]
            ver_2[2] = hor_2[2]
            ver_3[2] = hor_1[2]
            hor_1[2] = ver_1[6]
            hor_2[2] = ver_2[6]
            hor_3[2] = ver_3[6]
            ver_1[6] = hor_3[6]
            ver_2[6] = hor_2[6]
            ver_3[6] = hor_1[6]
            hor_1[6] = a
            hor_2[6] = b
            hor_3[6] = c
        else:
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = front[y][3-x-1]
            cpcp(front, dummy)
            a, b, c = ver_1[2], ver_2[2], ver_3[2]
            ver_1[2] = hor_1[6]
            ver_2[2] = hor_2[6]
            ver_3[2] = hor_3[6]
            hor_1[6] = ver_3[6]
            hor_2[6] = ver_2[6]
            hor_3[6] = ver_1[6]
            ver_1[6] = hor_1[2]
            ver_2[6] = hor_2[2]
            ver_3[6] = hor_3[2]
            hor_1[2] = c
            hor_2[2] = b
            hor_3[2] = a

    elif rot[0] == 'B':
        if rot[1] == '-':
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = behind[3-y-1][x]
            cpcp(behind, dummy)
            a, b, c = ver_1[0], ver_2[0], ver_3[0]
            ver_1[0] = hor_3[0]
            ver_2[0] = hor_2[0]
            ver_3[0] = hor_1[0]
            hor_1[0] = ver_1[8]
            hor_2[0] = ver_2[8]
            hor_3[0] = ver_3[8]
            ver_1[8] = hor_3[-1]
            ver_2[8] = hor_2[-1]
            ver_3[8] = hor_1[-1]
            hor_1[-1] = a
            hor_2[-1] = b
            hor_3[-1] = c
        else:
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = behind[y][3-x-1]
            cpcp(behind, dummy)
            a, b, c = ver_1[0], ver_2[0], ver_3[0]
            ver_1[0] = hor_1[-1]
            ver_2[0] = hor_2[-1]
            ver_3[0] = hor_3[-1]
            hor_1[-1] = ver_1[8]
            hor_2[-1] = ver_2[8]
            hor_3[-1] = ver_3[8]
            ver_1[8] = hor_1[0]
            ver_2[8] = hor_2[0]
            ver_3[8] = hor_3[0]
            hor_1[0] = c
            hor_2[0] = b
            hor_3[0] = a

    elif rot[0] == 'L':
        if rot[1] == '+':
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = left[3 - y - 1][x]
            cpcp(left, dummy)
            ver_1 = ver_1[-3:] + ver_1[:9]
        else:
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = left[y][3 - x - 1]
            cpcp(left, dummy)
            ver_1 = ver_1[3:] + ver_1[2:3] + ver_1[1:2] + ver_1[0:1]
        cp_part(hor_1, hor_2, hor_3, ver_1, ver_2, ver_3)

    elif rot[0] == 'R':
        if rot[1] == '+':
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = right[3 - y - 1][x]
            cpcp(right, dummy)
            ver_3 = ver_3[3:] + ver_3[2:3] + ver_3[1:2] + ver_3[0:1]
        else:
            for x in range(3):
                for y in range(3):
                    dummy[x][y] = right[y][3 - x - 1]
            cpcp(right, dummy)
            ver_3 = ver_3[-3:] + ver_3[:3]
        cp_part(hor_1, hor_2, hor_3, ver_1, ver_2, ver_3)
    if rot[0] != 'U':
        make_upper(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)
    if rot[0] != 'F':
        make_front(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)
    if rot[0] != 'D':
        make_lower(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)
    if rot[0] != 'B':
        make_behind(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)
    if rot[0] != 'L':
        make_left(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)
    if rot[0] != 'R':
        make_right(ver_1, ver_2, ver_3, hor_1, hor_2, hor_3)

N = int(input())
for _ in range(N):
    upper = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    lower = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    front = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    behind = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    left = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    right = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    ver_1 = ['w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y', 'o', 'o', 'o']
    ver_2 = ['w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y', 'o', 'o', 'o']
    ver_3 = ['w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y', 'o', 'o', 'o']
    hor_1 = ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b']
    hor_2 = ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b']
    hor_3 = ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b']
    M = int(input())
    rotate = list(input().split())
    for idx, r in enumerate(rotate):
        bingle(r)

        print("Iterate {0}".format(idx))
        print("Upper")
        for q in upper:
            print(q)
        print()
        print("Front")
        for q in front:
            print(q)
        print()
        print("Lower")
        for q in lower:
            print(q)
        print()
        print("Behind")
        for q in behind:
            print(q)
        print()
        print("Left")
        for q in left:
            print(q)
        print()
        print("Right")
        for q in right:
            print(q)
        '''
    for st in upper:
        print(st)
        '''
    print("==============================")
