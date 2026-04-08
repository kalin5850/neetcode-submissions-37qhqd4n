class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = k * threshold
        times = len(arr) - k + 1
        i, count = 0, 0
        while i < times:
            if sum(arr[i:i + k]) >= total:
                count += 1
            i += 1

        return count
