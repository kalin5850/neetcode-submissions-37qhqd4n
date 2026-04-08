class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        l, r = 0, 0
        window = {}
        while r < len(nums):
            if abs(r - l) > k:
                del window[nums[l]]
                l += 1
            if nums[r] in window:
                return True
            else:
                window[nums[r]] = 1
            r += 1
        
        return False

