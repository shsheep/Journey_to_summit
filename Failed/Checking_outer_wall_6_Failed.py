"""
# Greedy Trial
def clockwise_list(li: list, start: int, to: int):
    walls_idx = []
    if start + to >= len(li):
        circu = (start + to) % len(li)
        a = li[start:]
        b = li[:circu+1]
        for idx, w in enumerate(b):
            if w == 1:
                walls_idx.append(idx)
        for idx, w in enumerate(a):
            if w == 1:
                walls_idx.append(start+idx)
        return walls_idx
    else:
        a = li[start:start+to+1]
        for idx, w in enumerate(a):
            if w == 1:
                walls_idx.append(start+idx)
        return walls_idx


def backtrack(wall: list, dist: list, cnt: int):
    global answer
    if cnt >= answer:
        return
    print("Now cnt is {0} wall is {1}".format(cnt, wall))
    if 1 not in wall:
        print("Found it")
        answer = min(answer, cnt)
        return
    elif not dist:
        print("FAILED ", wall, dist, cnt)
        return

    friend = dist.pop()
    candidate = []
    max_cnt = 0
    for i in range(len(wall)):
        walls_idx = clockwise_list(wall, i, friend)
        tmp_num = len(walls_idx)
        # if tmp_num > 1:
        #     candidate.append(walls_idx)
        if max_cnt < tmp_num:
            candidate = [walls_idx]
            max_cnt = tmp_num
        # elif max_cnt == tmp_num or max_cnt - tmp_num <= 2: # TC 21 incorrect, 10 TLE
        elif max_cnt == tmp_num: # TC 21 correct, 10 incorrect
            if walls_idx not in candidate:
                candidate.append(walls_idx)
    print(candidate)
    for ws in candidate:
        print("ws is ", ws, "friend is ", friend)
        for idx in ws:
            wall[idx] = 0
        backtrack(wall, dist, cnt+1)
        for idx in ws:
            wall[idx] = 1
    dist.append(friend)


def solution(n, weak, dist):
    global answer
    dist.sort()
    wall = [0] * n
    for w in weak:
        wall[w] = 1
    print(wall)
    print(dist)
    answer = 0xFFFF
    backtrack(wall, dist, 0)
    if answer == 0xFFFF:
        answer = -1
    return answer
"""

import itertools

def solution(n, weak, dist):
    answer = 0xFFFF
    dist.sort()
    for num in range(1, len(dist)+1):
        for case in itertools.permutations(dist, num):
            for i, w in enumerate(weak):
                li_case = list(case)
                if i != 0:
                    tmp_weak = weak[i:] + [extended + n for extended in weak[:i]]
                else:
                    tmp_weak = weak.copy()
                init = 0
                cnt = 0
                while True:
                    if not li_case:
                        break
                    friend = li_case.pop()
                    cnt += 1
                    if cnt >= answer:
                        break
                    start = tmp_weak[init]
                    done = True
                    for jdx in range(init+1, len(tmp_weak)):
                        if tmp_weak[jdx] > start + friend:
                            done = False
                            init = jdx
                            break
                    if done:
                        answer = min(answer, cnt)
                        break
    if answer == 0xFFFF:
        answer == -1
    return answer





print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print("=========================================")
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print("=========================================")
print("WHY?")
print(solution(12, [1, 2, 3, 4, 5, 9, 10], [1, 1, 1]))
print("=========================================")
print("=========>WHY?")
print(solution(12, [1, 2, 3, 4, 5, 9, 10], [1, 1, 1, 1]))
print("=========================================")
print(solution(12, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11], [4, 3, 2, 11, 1]))
print("=========================================")
print(solution(16, [0, 3, 5, 6, 10, 9, 14], [1, 2, 3 ,4, 5]))
