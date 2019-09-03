import sys
sys.stdin = open("sample_input.txt", "r")

T = 10
for case in range(1, T+1):
    dummy = input()
    #print(dummy)
    ret = 0
    buildings = list(map(int, input().split()))
    # print(buildings)
    # print(len(buildings))
    for idx, b in enumerate(buildings):
        if idx <= 1 or idx >= len(buildings) - 2:
            continue
        left_block = max(buildings[idx - 1], buildings[idx - 2])
        right_block = max(buildings[idx + 1], buildings[idx + 2])
        if b > left_block and b > right_block:
            maximum = max(left_block, right_block)
            ret += b - maximum
        else:
            continue
    print("#{0} {1}".format(case, ret))