import sys
sys.stdin = open("sample_input.txt", "r")
import itertools

tmp = list(map(int, input().split()))
N, M = tmp

city = []
for _ in range(N):
    cat = input().split()
    city.append(cat)
# print(N, M)
# for row in city:
#     print(row)

home = []
kfc = []
for row in range(N):
    for col in range(N):
        if city[row][col] == '1':
            home.append((row, col))
        elif city[row][col] == '2':
            kfc.append((row, col))
# print(home)
# print(kfc)
cur_kfc = len(kfc)
if cur_kfc >= M:
    cmp_distance = []
    for select in itertools.combinations(kfc, M):
        distance = 0
        for h in home:
            each_min = 2 * N
            for chicken in select:
                each_min = min(abs(chicken[0] - h[0]) + abs(chicken[1] - h[1]), each_min)
            distance += each_min
        cmp_distance.append(distance)
print(min(cmp_distance))

