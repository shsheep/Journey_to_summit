from collections import deque

def solution(food_times, k):
    if k < len(food_times):
        return k+1
    if sum(food_times) <= k:
        return -1

    N = len(food_times)
    srtd_ft = []
    for i in range(len(food_times)):
        srtd_ft.append((food_times[i], i+1))
    srtd_ft = sorted(srtd_ft, key=lambda tup: tup[0])
    srtd_ft = deque(srtd_ft)
    # print(srtd_ft)

    len_to_eat = len(srtd_ft)
    total_eaten = 0
    prev_food = 0
    while total_eaten + (srtd_ft[0][0]-prev_food) * len_to_eat <= k:
        cur_food = srtd_ft.popleft()[0]
        total_eaten += (cur_food - prev_food) * len_to_eat
        len_to_eat -= 1
        prev_food = cur_food
    # print(srtd_ft, total_eaten)
    result = sorted(srtd_ft, key=lambda tup: tup[1])
    # print(result)
    ret = result[(k-total_eaten) % len_to_eat][1]
    return ret


print(solution([3, 1, 2], 5))  # => 1
print(solution([10, 4, 6], 17))  # => (6, 0, 2) 5
