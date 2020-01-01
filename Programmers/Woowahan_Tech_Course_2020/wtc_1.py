def distance(rest: list, r: list):
    return ((rest[0] - r[0]) ** 2 + (rest[1] - r[1]) ** 2) ** 0.5

def solution(restaurant, riders, k):
    answer = 0
    for r in riders:
        if distance(restaurant, r) <= float(k):
            answer += 1
    return answer


print(solution([0, 0], [[-700,0], [150,180], [500,500], [150, -800], [800, 800], [-900, 500], [-1100, 900]], 1000))