class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        # dp = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]
        # for i in range(1, len(profit) + 1):
        #     for w in range(1, capacity + 1):
        #         if w - weight[i - 1] >= 0:
        #             dp[i][w] = max(
        #                 dp[i - 1][w], profit[i - 1] + dp[i][w - weight[i - 1]]
        #             )
        #         else:
        #             dp[i][w] = dp[i - 1][w]
        # return dp[len(profit)][capacity]
        def diff_tree(capa: int, cache) -> int:
            """
            Brute Force Solution:
                Time Complexity: O(2^N)
                Space Complexity: O(N)
                where N is the number of items
            """
            if capa <= 0:
                return 0
            if capa in cache:
                return cache[capa]

            best = 0
            for i in range(len(profit)):
                if capa >= weight[i]:
                    best = max(best, diff_tree(capa - weight[i], cache) + profit[i])
                    cache[capa] = best

            return best

        return diff_tree(capacity, {})