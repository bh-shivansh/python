class MaximumProfitFinder:
    def maximumProfit(self, list, fees):
        def cost(i, n, prev):
            if i >= n:
                return 0
            elif prev == True:
                return max(cost(i+1, n, False) + prices[i] - fees, cost(i + 1, n, prev))
            else:
                return max(cost(i+1, n, True) - prices[i], cost(i + 1, n, prev))
        return cost(0, len(prices), False)


profit = MaximumProfitFinder()
prices = [10, 20, 30, 40, 50]
print(profit.maximumProfit(prices, fees=15))