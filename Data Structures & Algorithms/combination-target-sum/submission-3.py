class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def dfs(target, path, result, i):
            if i == len(nums):
                return result
            if target == 0:
                result.append(path.copy())
                return result
            target -= nums[i]
            if target < 0:
                return result
            path.append(nums[i])
            dfs(target, path, result, i)
            path.pop()
            target += nums[i]
            dfs(target, path, result, i + 1)

            return result

        return dfs(target, [], [], 0)
