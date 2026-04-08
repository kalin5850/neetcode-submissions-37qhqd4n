class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        l, r = 0, 1
        while r < len(nums):
            if abs(r - l) > k:
                l += 1
                tmp = l
                while tmp < r:
                    if nums[tmp] == nums[r]:
                        return True
                    tmp += 1
            if nums[l] == nums[r]:
                return True
            r += 1
        
        return False

