def solution(stones, k):
    # Maximum possible people
    answer = 200000000
    i = -1
    # From idx -1 ~ len(stones)-k-1,
    # checking the maximum stepping times
    while i < len(stones)-k:
        if i == -1:
            if answer > max(stones[:k]):
                answer = max(stones[:k])
            idx = stones[:k].index(max(stones[:k]))
            # Skip the overlapped section
            # which results the same maximum stepping times from before iteration
            i += idx+1
            continue
        elif i == len(stones)-k-1:
            if answer > max(stones[len(stones)-k:]):
                answer = max(stones[len(stones)-k:])
            idx = stones[len(stones)-k:].index(max(stones[len(stones)-k:]))
            i += idx+1
            continue
        else:
            if answer > max(stones[i+1:i+k+1]):
                answer = max(stones[i+1:i+k+1])
            idx = stones[i+1:i+k+1].index(max(stones[i+1:i+k+1]))
            i += idx+1
            continue
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# 2, 4, 5, 3, 2, 1, 4, 2, 5, 1
# 1, 3, 4, 2, 1, 0, 3, 1, 4, 0 -> 1
# 0, 2, 3, 1, 0, 0, 2, 0, 3, 0 -> 2
# 0, 1, 2, 0, 0, 0, 1, 0, 2, 0 -> 3
# 0, 0, 1, 0, 0, 0, 1, 0, 2, 0
#                ^

# def solution(stones, k):
#     # Maximum possible people
#     answer = 200000000
#     i = -1
#     # From idx -1 ~ len(stones)-k-1,
#     # checking the maximum stepping times
#     while i < len(stones)-k:
#         if i == -1:
#             if answer > max(stones[:k]):
#                 answer = max(stones[:k])
#             idx = stones[:k].index(max(stones[:k]))
#             # Skip the overlapped section
#             # which results the same maximum stepping times from before iteration
#             i += idx+1
#             continue
#         elif i == len(stones)-k-1:
#             if answer > max(stones[len(stones)-k:]):
#                 answer = max(stones[len(stones)-k:])
#             idx = stones[len(stones)-k:].index(max(stones[len(stones)-k:]))
#             i += idx+1
#             continue
#         else:
#             if answer > max(stones[i+1:i+k+1]):
#                 answer = max(stones[i+1:i+k+1])
#             idx = stones[i+1:i+k+1].index(max(stones[i+1:i+k+1]))
#             i += idx+1
#             continue
#     return answer

