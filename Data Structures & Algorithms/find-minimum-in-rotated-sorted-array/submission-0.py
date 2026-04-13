class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        for i in range(1, len(nums)):
            min_val = min(min_val, nums[i])

        return min_val