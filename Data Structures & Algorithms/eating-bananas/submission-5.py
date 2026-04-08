import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        last_middle = -1
        while l <= r:
            m = (l + r) // 2
            tmp = [math.ceil(x / m) for x in piles]
            k = sum(tmp)
            print(f"{m} ==== {k} === {tmp} === {l} ==== {r}")
            if k > h:
                l = m + 1
            elif k <= h:
                r = m - 1
                last_middle = m
        
        return last_middle