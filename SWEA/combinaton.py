import time
import itertools

def dfs_comb(position: int):
    if len(to_print) == num:
        print(to_print)
        return
    for i in range(position, len(li)):
        to_print.append(li[i])
        dfs_comb(i + 1)
        to_print.pop()

# li = list(map(int, input('List -> ').split()))
# num = int(input('to select -> '))
li = [i for i in range(25)]
num = 10
print(li, num)
to_print = []
start = time.time()
dfs_comb(0)
end = time.time()
time_1 = end-start

start = time.time()
for case in itertools.combinations(li, num):
    print(case)
end = time.time()
time_2 = end-start

print(time_1, time_2)