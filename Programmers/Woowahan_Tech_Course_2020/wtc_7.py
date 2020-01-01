from collections import defaultdict

def solution(user, friends, visitors):
    friend_dict = defaultdict(lambda: [])
    for tx in friends:
        f1, f2 = tx
        friend_dict[f1].append(f2)
        friend_dict[f2].append(f1)
    my_friend = []
    for key in friend_dict.keys():
        friend_dict[key] = list(set(friend_dict[key]))
        if key == user:
            my_friend = friend_dict[key]

    each_score = defaultdict(lambda: 0)
    for key in friend_dict.keys():
        if key == user:
            continue
        for fr in my_friend:
            if fr in friend_dict[key]:
                each_score[key] += 10

    for vis in visitors:
        if vis in my_friend:
            continue
        each_score[vis] += 1

    print(friend_dict)
    print(each_score)
    to_sort = defaultdict(lambda: [])

    answer = []
    for key in each_score.keys():
        to_sort[each_score[key]].append(key)
    tskeys = list(to_sort.keys())
    tskeys.sort(reverse=True)
    for score in tskeys:
        to_sort[score].sort()
        answer += to_sort[score]

    return answer

print(solution("mrko", [["donut", "andole"], ["donut", "jun"], ["donut", "mrko"], ["shakevan", "andole"], ["shakevan", "jun"], ["shakevan", "mrko"]], ["bedi", "bedi", "donut", "bedi", "shakevan"]))
