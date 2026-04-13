import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_buy = prices[0]

        for sell in prices:
            max_p = max(max_p, sell - min_buy)
            min_buy = min(sell, min_buy)

        return max_p