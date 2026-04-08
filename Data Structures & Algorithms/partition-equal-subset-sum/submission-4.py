class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        
        def dfs(i: int, cur_sum: int) -> bool:
            if cur_sum == target:
                return True
            if cur_sum > target or i == len(nums):
                return False
            
            
            return dfs(i + 1, cur_sum + nums[i]) or dfs(i + 1, cur_sum)
        
        return dfs(0, 0)