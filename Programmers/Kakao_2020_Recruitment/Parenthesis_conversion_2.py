def check_right(pth: str):
    depth = 0
    for p in pth:
        if p == '(':
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return True


def check_balanced(pth: str):
    depth = 0
    for p in pth:
        if p == '(':
            depth += 1
        else:
            depth -= 1
    return depth == 0


def divide(pth: str):
    for i in range(1, len(pth)-1):
        u, v = pth[:i], pth[i:]
        if not(check_balanced(u) and check_balanced(v)):
            continue
        else:
            # print(i, divide(u))
            if not divide(u):
                return u, v


def solution(p):
    if not p:
        return p
    if check_right(p):
        return p
    if divide(p):
        u, v = divide(p)
    else:
        u = p
        v = ''
    if check_right(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        tmp = ''
        for i, st in enumerate(u):
            if i == 0 or i == len(u) - 1:
                continue
            to_append = ')' if st == '(' else '('
            tmp += to_append
        answer += tmp
    return answer

m = input()
print(solution(m))