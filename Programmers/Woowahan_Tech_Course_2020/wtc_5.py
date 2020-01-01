# Recipe : jok: -4kg, onion: -50g, green: -10cm, garlic: -10g, pepper: -4g or -2g
# Price: jok: 10000/10kg, onion: 3000/100g, green: 1000/30cm, garlic: 2000/50g, pepper: 1000/10g

def solution(history):
    ingredients = [5, 100, 10, 5, 2]
    needing_ingredients = [4, 50, 10, 10, 4]
    amount = [10, 100, 30, 50, 10]
    prices = [10000, 3000, 1000, 2000, 1000]
    answer = []
    for h in history:
        budget = 0
        h = float(h)
        if h > 2.5 or h <= 0.5:
            return [-1]

        june, with_gf = h // 1.0, h % 1.0
        # With girlfriend - half pepper needed
        if with_gf:
            for i in range(5):
                # When calculating the pepper
                if i == 4:
                    if needing_ingredients[i] * june + needing_ingredients[i] / 2 * with_gf > ingredients[i]:
                        how_many = ((needing_ingredients[i] * june + needing_ingredients[i] / 2 * with_gf) - ingredients[i]) // amount[i] + 1
                        budget += prices[i] * how_many
                        ingredients[i] = ingredients[i] - needing_ingredients[i] * june - needing_ingredients[i] / 2 * with_gf + amount[i] * how_many
                    else:
                        ingredients[i] -= needing_ingredients[i] * june + needing_ingredients[i] / 2 * with_gf

                # When not the pepper
                else:
                    if needing_ingredients[i] * (june+with_gf) > ingredients[i]:
                        how_many = ((needing_ingredients[i] * (june+with_gf)) - ingredients[i]) // amount[i] + 1
                        budget += prices[i] * how_many
                        ingredients[i] = ingredients[i] - needing_ingredients[i] * (june+with_gf) + amount[i] * how_many
                    else:
                        ingredients[i] -= needing_ingredients[i] * (june+with_gf)

        # Only June - whole pepper
        else:
            for i in range(5):
                if needing_ingredients[i] * june > ingredients[i]:
                    how_many = ((needing_ingredients[i]*june-ingredients[i]) // amount[i])+1
                    budget += prices[i] * how_many
                    ingredients[i] = ingredients[i] - needing_ingredients[i] * june + amount[i] * how_many
                else:
                    ingredients[i] -= needing_ingredients[i] * june

        answer.append(budget)

    return answer

print(solution(["1.0", "2.0", "1.5"]))
print(solution(["1.0", "2.0", "0.0", "1.0"]))
