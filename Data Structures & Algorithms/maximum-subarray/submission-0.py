class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = nums[0], nums[0]
        l = 0
        for r in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[r]
            maxSum = max(curSum, maxSum)

        return maxSum    
