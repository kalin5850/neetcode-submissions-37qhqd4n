class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]
        for i in range(1, len(profit) + 1):
            for w in range(1, capacity + 1):
                if w - weight[i - 1] >= 0:
                    dp[i][w] = max(
                        dp[i - 1][w], profit[i - 1] + dp[i - 1][w - weight[i - 1]]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[len(profit)][capacity]
            