def solution(prices, discounts):
    answer = 0
    prices.sort(reverse=True)
    discounts.sort(reverse=True)
    p_idx = 0
    for d in discounts:
        if p_idx >= len(prices):
            return int(answer)
        answer += float(prices[p_idx]) * (100 - d) / 100
        p_idx += 1
    answer += sum(prices[p_idx:])
    answer = int(answer)
    return answer

print(solution([13000, 88000, 10000], [30, 20]))
print(solution([32000, 18000, 42500], [50, 20, 65]))
