from itertools import combinations
from collections import defaultdict

def solution(relation):
    R, C = len(relation), len(relation[0])
    columns = [num for num in range(C)]
    ck_keys = []
    answer_li = []
    for num in range(1, C+1):
        for case in combinations(columns, num):
            cond_2 = True
            for ans in answer_li:
                if len(ans) == 1:
                    continue
                cnt = 0
                for c in case:
                    if c in ans:
                        cnt += 1
                if cnt == len(ans):
                    cond_2 = False
                    break
            if not cond_2:
                continue
            visited = defaultdict(lambda: False)
            is_ck = True
            for r in relation:
                tmp = ()
                for c in case:
                    tmp += (r[c],)
                if visited[tmp]:
                    is_ck = False
                    break
                else:
                    visited[tmp] = True
            if is_ck:
                for c in case:
                    ck_keys.append(c)
                answer_li.append(case)
                if len(case) == 1:
                    columns.remove(case[0])
                continue
    answer = len(answer_li)
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
