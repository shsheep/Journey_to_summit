def concat(li: list):
    ret = ''
    for st in li:
        ret += st
    return ret

def compression(rep: int, word: str):
    ret = []
    already = False
    compressed = False
    tmp1 = []
    tmp2 = []
    div = len(word) // rep * rep
    for i in range(div):
        last_appended = False
        if len(tmp1) != rep:
            tmp1.append(word[i])
        elif len(tmp2) != rep:
            tmp2.append(word[i])
            if already and tmp2[0] != tmp1[0]:
                already = False
                tmp1 = tmp2
                tmp2 = []
        if len(tmp1) == rep and len(tmp2) == rep:
            if tmp1 and tmp2 and tmp1 == tmp2:
                compressed = True
                if already:
                    cnt = ret[-1 * rep - 1]
                    ret[-1 * rep - 1] = str(int(cnt) + 1)

                    tmp1 = tmp2
                    tmp2 = []
                else:
                    ret.append('2')
                    ret += tmp1
                    tmp2 = []
                    already = True
                last_appended = True
            elif tmp1 != tmp2:
                if already:
                    already = False
                else:
                    ret += tmp1
                tmp1 = tmp2
                tmp2 = []
    if not last_appended:
        ret += tmp1
    remain = len(word) % rep
    if remain != 0:
        ret += list(word[-remain:])

    if not compressed:
        return word

    return concat(ret)

def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    for i in range(1, len(s) // 2 + 1):
        tmp = compression(i, s)
        answer = min(len(tmp), answer)
    return answer