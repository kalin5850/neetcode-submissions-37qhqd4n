class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            tmp = 1
            for j in range(len(nums)):
                if i != j:
                    tmp *= nums[j]
            res.append(tmp)
        
        return res