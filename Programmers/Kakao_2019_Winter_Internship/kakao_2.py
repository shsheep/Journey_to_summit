import re

def solution(s):
    s = s[1:-1]
    p = re.compile('[0-9]+')
    li = s.split('},')
    collected = []
    for l in li:
        result = p.findall(l)
        result = list(map(int, result))
        collected.append(result)
    print(collected)
    collected.sort(key=lambda each: len(each))
    print(collected)

    answer = []
    for c in collected:
        if len(c) == 1:
            answer.append(c[0])
            continue
        c = list(filter(lambda num: num not in answer, c))
        answer += c

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
