class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, capacity):
            if i == len(profit) or capacity <= 0:
                return 0
            
            if weight[i] > capacity:
                return dfs(i + 1, capacity)
            else:
                include = dfs(i, capacity - weight[i]) + profit[i]
                exclude = dfs(i + 1, capacity)

            return max(include, exclude)
        
        return dfs(0, capacity)