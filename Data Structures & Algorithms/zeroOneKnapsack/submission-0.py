class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def helper(i, profit, weight, capacity):
            if i == len(profit) or capacity == 0:
                return 0
            
            if weight[i] > capacity:
                return helper(i + 1, profit, weight, capacity)
            else:
                include = profit[i] + helper(i + 1, profit, weight, capacity - weight[i])
                exclude = helper(i + 1, profit, weight, capacity)

                return max(include, exclude)
        
        return helper(0, profit, weight, capacity)
            