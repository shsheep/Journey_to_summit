import sys
sys.stdin = open("sample_input.txt", "r")

global memo

def doSomething(tmp_ret: str, i: int, j: int):
    if i < 0 or j < 0 or i >= 4 or j >= 4:
        return
    tmp_ret += theMap[i][j]
    if len(tmp_ret) == 7:
        memo.append(tmp_ret)
        return
    for x in range(4):
        if x == 0:
            doSomething(tmp_ret, i-1, j)
        elif x == 1:
            doSomething(tmp_ret, i, j+1)
        elif x == 2:
            doSomething(tmp_ret, i+1, j)
        else:
            doSomething(tmp_ret, i, j-1)

T = int(input())
for case in range(1, T+1):
    theMap, memo = [], []
    for _ in range(4):
        theMap.append(input().split())
    # print(theMap)
    for i in range(4):
        for j in range(4):
            tmp_ret = ''
            doSomething(tmp_ret, i, j)
    # print(memo)
    set_memo = set(memo)
    # print(set_memo)
    ret = len(set_memo)
    print("#{0} {1}".format(case, ret))