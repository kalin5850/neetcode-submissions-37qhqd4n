import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        last_middle = -1
        while l <= r:
            m = (l + r) // 2
            k = sum(math.ceil(x / m) for x in piles)
            if k > h:
                l = m + 1
            elif k <= h:
                r = m - 1
                last_middle = m
        
        return last_middle