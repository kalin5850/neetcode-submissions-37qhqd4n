import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q, res = [], []
        count = Counter(nums)

        for key, value in count.items():
            heapq.heappush(q, (-value, key))

        while k > 0:
            value, key = heapq.heappop(q)
            res.append(key)
            k -= 1
        
        return res