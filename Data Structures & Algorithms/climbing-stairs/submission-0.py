class Solution:
    def climbStairs(self, n: int) -> int:
        def count(n: int) -> int:
            if n <= 1:
                return 1
            return count(n - 1) + count(n - 2)
        
        return count(n)