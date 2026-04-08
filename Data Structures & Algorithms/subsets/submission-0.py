class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(idx: int, path: list[int], result: list[list[int]]):
            if idx == len(nums):
                print(path)
                result.append(path.copy())
                return result
            dfs(idx + 1, path, result)
            path.append(nums[idx])
            dfs(idx + 1, path, result)
            path.pop()
            
            return result
        
        result = dfs(0, [], [])
        return result