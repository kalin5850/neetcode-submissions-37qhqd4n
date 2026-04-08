class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(idx: int, path: list[int], result: list[list[int]]):
            if idx == len(nums):
                result.append(path.copy())
                return result
            dfs(idx + 1, path, result)
            path.append(nums[idx])
            dfs(idx + 1, path, result)
            path.pop()
            
            return result
        
        return dfs(0, [], [])