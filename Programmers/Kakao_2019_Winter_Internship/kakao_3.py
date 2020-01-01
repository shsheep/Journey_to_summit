from collections import defaultdict


# Compare the two string with same length considering the '*' letter
# If those are same, return True
def compare(uid: str, bid: str):
    for i in range(len(uid)):
        if bid[i] == '*':
            continue
        if uid[i] != bid[i]:
            return False
    return True


def dfs(banned_id: list, user_id: list, bid_dict: dict, cnt: int, prog: list):
    global whole_case
    if cnt >= len(banned_id):
        to_append = prog.copy()
        to_append.sort()
        if whole_case[tuple(to_append)]:
            print("VISITED")
            return
        whole_case[tuple(to_append)] = True

        print("FIND IT", to_append)
        return
    bid = banned_id[cnt]
    for candi in bid_dict[bid]:
        idx = candi[1]
        if not user_id[idx][1]:
            user_id[idx][1] = True
            prog.append(user_id[idx][0])

            tmp = prog.copy()
            tmp.sort()
            # if visited[tuple(tmp)]:
            #     user_id[idx][1] = False
            #     prog.pop()
            #     continue

            print("PROGRESS IS ", prog)
            dfs(banned_id, user_id, bid_dict, cnt+1, prog)
            user_id[idx][1] = False
            prog.pop()


def solution(user_id, banned_id):
    global whole_case
    whole_case = defaultdict(lambda: False)
    answer = 0
    bid_dict = defaultdict(lambda: [])
    user_id = [[uid, False] for uid in user_id]
    # To avoid overlapped case, make the banned_id as Set
    for bid in set(banned_id):
        for idx, uid in enumerate(user_id):
            if len(uid[0]) != len(bid):
                continue
            if compare(uid[0], bid):
                bid_dict[bid].append((uid[0], idx))

    for k in bid_dict.keys():
        print("{0} : {1}".format(k, bid_dict[k]))
    print(banned_id)
    dfs(banned_id, user_id, bid_dict, 0, [])
    print("WHOLE CASE IS ", whole_case)
    for st in whole_case.keys():
        if whole_case[st]:
            answer += 1
    # answer = len(whole_case.keys())
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

# from collections import defaultdict
#
#
# # Compare the two string with same length considering the '*' letter
# # If those are same, return True
# def compare(uid: str, bid: str):
#     for i in range(len(uid)):
#         if bid[i] == '*':
#             continue
#         if uid[i] != bid[i]:
#             return False
#     return True
#
#
# def dfs(banned_id: list, user_id: list, bid_dict: dict, cnt: int, prog: list):
#     global whole_case
#     # If all banned_id is selected, check whether it's already checked
#     # and add to answer
#     if cnt >= len(banned_id):
#         to_append = prog.copy()
#         to_append.sort()
#         if whole_case[tuple(to_append)]:
#             return
#         whole_case[tuple(to_append)] = True
#         return
#
#     # For candidates of current selected banned_id,
#     bid = banned_id[cnt]
#     for candi in bid_dict[bid]:
#         idx = candi[1]
#         # If it is not already chosen,
#         if not user_id[idx][1]:
#             user_id[idx][1] = True
#             prog.append(user_id[idx][0])
#             tmp = prog.copy()
#             tmp.sort()
#             # Double check for overlapping cases . . . not neccessary maybe
#             if whole_case[tuple(tmp)]:
#                 user_id[idx][1] = False
#                 prog.pop()
#                 continue
#             dfs(banned_id, user_id, bid_dict, cnt + 1, prog)
#             # Restoration for backtracking
#             user_id[idx][1] = False
#             prog.pop()
#
#
# def solution(user_id, banned_id):
#     global whole_case
#     whole_case = defaultdict(lambda: False)
#     answer = 0
#     bid_dict = defaultdict(lambda: [])
#     user_id = [[uid, False] for uid in user_id]
#     # To avoid overlapped case, make the banned_id as Set
#     for bid in set(banned_id):
#         for idx, uid in enumerate(user_id):
#             if len(uid[0]) != len(bid):
#                 continue
#             if compare(uid[0], bid):
#                 # Save the all matching case in bid_dict Dictionary
#                 bid_dict[bid].append((uid[0], idx))
#     dfs(banned_id, user_id, bid_dict, 0, [])
#     # Sort the normal cases
#     for st in whole_case.keys():
#         if whole_case[st]:
#             answer += 1
#     return answer
