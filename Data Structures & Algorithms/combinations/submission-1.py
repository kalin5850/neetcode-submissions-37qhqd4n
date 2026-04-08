class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(idx, cur, result):
            if len(cur) == k:
                result.append(cur.copy())
                return result
            if idx > n:
                return
            
            for j in range(idx, n + 1):
                cur.append(j)
                dfs(j + 1, cur, result)
                cur.pop()
            
            return result
        
        return dfs(1, [], [])