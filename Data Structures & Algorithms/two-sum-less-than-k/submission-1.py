class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_t = -1
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] >= k:
                r -= 1
            else:
                max_t = max(max_t, nums[l] + nums[r])
                l += 1
        
        return max_t