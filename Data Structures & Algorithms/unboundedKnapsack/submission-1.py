class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, capacity):
            if i == len(profit) or capacity <= 0:
                return 0
            
            # exclude
            max_profit = dfs(i + 1, capacity)
            new_cap = capacity - weight[i]
            if new_cap >= 0:
                include = dfs(i, capacity - weight[i]) + profit[i]
                max_profit = max(max_profit, include)
            
            return max_profit
        
        return dfs(0, capacity)