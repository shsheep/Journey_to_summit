def solution(forms):
    word_dict = dict()

    for f in forms:
        existing = []
        nick = f[1]
        for i in range(len(nick)-1):
            tmp = nick[i:i+2]
            if tmp in existing:
                continue
            if tmp in word_dict:
                word_dict[tmp] += 1
            else:
                word_dict[tmp] = 1
            existing.append(tmp)
    print(word_dict)
    keys = list(word_dict.keys())
    keys = list(filter(lambda word: word_dict[word] > 1, keys))
    print(keys)
    answer = []
    for k in keys:
        for f in forms:
            if k in f[1]:
                answer.append(f[0])
    answer = list(set(answer))
    answer.sort()

    return answer

print(solution([["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"], ["woniee@email.com", "워니"], ["mj@email.com", "엠제이"], ["nowm@email.com", "이제엠"]]))
