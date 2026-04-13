class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0 
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] - prices[r] > 0:
                l, r = r, r + 1
            else:
                max_p = max(max_p, abs(prices[l] - prices[r]))
                r += 1
        
        return max_p