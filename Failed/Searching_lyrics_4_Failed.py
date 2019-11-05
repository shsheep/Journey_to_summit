class node:
    def __init__(self, ch: str, cnt: int, child: list):
        self.ch = ch
        self.cnt = cnt
        self.child = child

def solution(words, queries):
    answer = []
    trie = [None] * 100001
    rev_trie = [None] * 100001
    for w in words:
        idx = len(w)
        if not trie[idx] and not rev_trie[idx]:
            trie[idx] = node(None, 0, [])
            rev_trie[idx] = node(None, 0, [])
        tmp = trie[idx]
        for j, ch in enumerate(w):
            if not tmp.child:
                newnode = node(ch, 1, [])
                tmp.child.append(newnode)
                tmp = tmp.child[-1]
            else:
                flag = False
                for k, child in enumerate(tmp.child):
                    if child.ch == ch:
                        child.cnt += 1
                        flag = True
                        tmp = tmp.child[k]
                if not flag:
                    newnode = node(ch, 1, [])
                    tmp.child.append(newnode)
                    tmp = tmp.child[-1]
        tmp = rev_trie[idx]
        for i in range(len(w)-1, -1, -1):
            if not tmp.child:
                newnode = node(ch, 1, [])
                tmp.child.append(newnode)
                tmp = tmp.child[-1]
            else:
                flag = False
                for k, child in enumerate(tmp.child):
                    if child.ch == ch:
                        child.cnt += 1
                        flag = True
                        tmp = tmp.child[k]
                if not flag:
                    newnode = node(ch, 1, [])
                    tmp.child.append(newnode)
                    tmp = tmp.child[-1]
    for q in queries:
        if q[0] == '?':
            tmp_q = ''.join(reversed(q))
            cur = rev_trie[len(tmp_q)]
            if not cur:
                answer.append(0)
                continue
            idx = 0
            while tmp_q[idx] != '?':
                flag = False
                for i, n in enumerate(cur.child):
                    if n.ch == tmp_q[idx]:
                        cnt = cur.child[i].cnt
                        cur = cur.child[i]
                        idx += 1
                        flag = True
                        break
                if not flag:
                    answer.append(0)
                    break
            if flag:
                answer.append(cnt)
        else:
            cur = trie[len(q)]
            if not cur:
                answer.append(0)
                continue
            idx = 0
            while q[idx] != '?':
                flag = False
                for i, n in enumerate(cur.child):
                    if n.ch == q[idx]:
                        cnt = cur.child[i].cnt
                        cur = cur.child[i]
                        idx += 1
                        flag = True
                        break
                if not flag:
                    answer.append(0)
                    break
            if flag:
                answer.append(cnt)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
print(solution(["apple", "appld", "applac", "apldc", "applecd", "banana", "ban", "bandxd","bantyz", "con", "cold", "colq", "coola"], ["ap???", "??n", "ban???", "xyz?"]))

# ["apple", "appld", "applac", "apldc", "applecd", "banana", "ban", "bandxd",
# "bantyz", "con", "cold", "colq", "coola"], ["ap???", "??n", "ban???"]