class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        l, count = 0, 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                total -= arr[l]
                l += 1
            total += arr[r]
            if total >= k * threshold and r - l + 1 == k:
                count += 1

        return count
