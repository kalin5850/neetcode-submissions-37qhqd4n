class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ## brute force
        # if sum(nums) % 2 != 0:
        #     return False
        # target = sum(nums) // 2
        
        # def dfs(i: int, cur_sum: int) -> bool:
        #     if cur_sum == target:
        #         return True
        #     if cur_sum > target or i == len(nums):
        #         return False
            
            
        #     return dfs(i + 1, cur_sum + nums[i]) or dfs(i + 1, cur_sum)
        
        # return dfs(0, 0)

        ## Memorization
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        cache = [[-1] * (target + 1)] * (len(nums) + 1)

        def dfs_cache(i, cur_sum):
            if cur_sum == target:
                return True
            if cur_sum > target or i == len(nums):
                return False
            if cache[i][cur_sum] != -1:
                return cache[i][cur_sum]
            cache[i][cur_sum] = (dfs_cache(i + 1, cur_sum + nums[i]) or
                                dfs_cache(i + 1, cur_sum))
            
            return cache[i][cur_sum]

        result = dfs_cache(0, 0)
        print(cache)

        return result




