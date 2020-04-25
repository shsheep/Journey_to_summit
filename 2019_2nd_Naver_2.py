from functools import reduce


def valueOf(array: list):
    return reduce(lambda a,b: a*b, array)


# 2, [1,2] => [2,3]
def getNextPattern(array: list):
    array.pop(0)
    array.append(array[-1]+1)
    newArray = array[:]
    return newArray


def initGrowthPattern(patternGrowth: int):
    return list(range(1, patternGrowth+1))


def solve(n: int):
    patternMap = { 2: [1,2] }

    index = 0
    answer = 0
    patternGrowth = 2
    while(index < n):
        minPattern = min(patternMap.items(), key=lambda x: valueOf(x[1]))
        patternIdx, selectedPattern = minPattern

        if (selectedPattern[0] == 2):
            patternGrowth += 1
            patternMap[patternGrowth] = initGrowthPattern(patternGrowth)

        if (answer == valueOf(selectedPattern)):
            patternMap[patternIdx] = getNextPattern(selectedPattern)
            continue

        answer = valueOf(selectedPattern)
        patternMap[patternIdx] = getNextPattern(selectedPattern)

        index += 1

    return answer


if __name__ == "__main__":
    answers = [0, 2, 6, 12, 20, 24, 30, 42, 56, 60, 72]
    solve(5)

    for n, answer in enumerate(answers):
        assert solve(n) is answer, "n: %s, want: %s, actual: %s" % (n, answer, solve(n))
