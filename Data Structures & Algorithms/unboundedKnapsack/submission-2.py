class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs_cache(i, capacity, cache):
            if i == len(profit) or capacity <= 0:
                return 0
            if (i, capacity) in cache:
                return cache[(i, capacity)]
            
            exclude_val = dfs_cache(i + 1, capacity, cache)
            include_val = -1
            if weight[i] <= capacity:
                include_val = dfs_cache(i, capacity - weight[i], cache) + profit[i]
            cache[(i, capacity)] = max(exclude_val, include_val)

            return cache[(i, capacity)]
        
        return dfs_cache(0, capacity, {})