class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        i = 0
        while i < k:
            result = -heapq.heappop(max_heap)
            i += 1

        return result