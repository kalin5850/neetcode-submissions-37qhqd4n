class Solution:
    def climbStairs(self, n: int) -> int:
        # """ recursion """
        # def count(n: int) -> int:
        #     if n <= 1:
        #         return 1
        #     return count(n - 1) + count(n - 2)
        
        # return count(n)

        """ recursion with cache """
        def count(n, cache):
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = count(n - 1, cache) + count(n - 2, cache)

            return cache[n]
        
        return count(n, {})