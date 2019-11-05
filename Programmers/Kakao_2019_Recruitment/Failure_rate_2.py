def solution(N, stages):
    memo = []
    stages.sort()
    #print(stages)
    start_stage = stages[0]
    for num in range(1, start_stage):
        memo.append((0.0, num))
    #print("memo is ", memo)
    while len(memo) < N:
        if start_stage not in stages:
            print("pass")
            memo.append((0.0, start_stage))
            start_stage += 1
            continue
        start_idx = stages.index(start_stage)
        stages = stages[start_idx:]
        #print("Refined stage is ", stages)
        players = len(stages)
        losers = 0
        for idx, st in enumerate(stages):
            if start_stage == st:
                losers += 1
        #print("the number of loser ", losers)
        memo.append((float(losers) / players, start_stage))
        start_stage += 1
    memo.sort(key=lambda rate: rate[0], reverse=True)
    #print("memo is ", memo)
    tmp = [stage[1] for stage in memo]
    return tmp
