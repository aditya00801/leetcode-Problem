class Solution(object):
    def maximumSaleItems(self, items, budget):
        cheapest = min(price for _, price in items)
        dp = [0] * (budget + 1)

        for i, (factor, price) in enumerate(items):
            free = sum(
                1 for j, (other_factor, _) in enumerate(items)
                if i != j and other_factor % factor == 0
            )

            for spent in range(budget, price - 1, -1):
                dp[spent] = max(dp[spent], dp[spent - price] + 1 + free)

        return max(
            dp[spent] + (budget - spent) // cheapest
            for spent in range(budget + 1)
        )