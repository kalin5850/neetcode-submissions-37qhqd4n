class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(idx, cur, result):
            if len(cur) == k:
                result.append(cur.copy())
                return result
            if idx > n:
                return
            
            cur.append(idx)
            dfs(idx + 1, cur, result)
            cur.pop()
            dfs(idx + 1, cur, result)
            
            return result
        
        return dfs(1, [], [])