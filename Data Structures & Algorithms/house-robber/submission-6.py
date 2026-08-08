class Solution:
    def rob(self, nums: List[int]) -> int:
        # result = []


        # def brute_force(i: int, total: int, res: list[int]) -> None:
        #     """
        #     Brute Force Solution:
        #         Time Complexity: O(2^N)
        #         Space Complexity: O(N + 2^N)
        #         where N is the number of items
        #     """
        #     # Base case: reached end of houses
        #     if i >= len(nums):
        #         res.append(total)
        #         return

        #     # Option 1: Rob house i, skip to i+2 (can't rob adjacent)
        #     brute_force(i + 2, total + nums[i], res)

        #     # Option 2: Skip house i, move to i+1
        #     brute_force(i + 1, total, res)


        # brute_force(0, 0, result)

        # return max(result)

        # def brute_force2(i: int, total: int) -> int:
        #     """
        #     Brute Force Solution:
        #         Time Complexity: O(2^N)
        #         Space Complexity: O(N)
        #         where N is the number of items
        #     """
        #     # Base case: reached end of houses
        #     if i >= len(nums):
        #         return 0

        #     return max(
        #         nums[i] + brute_force2(i + 2, total),  # Rob house
        #         brute_force2(i + 1, total)  # Skip house
        #     )

        # return brute_force2(0, 0)

        # def memorization(i: int, cache: dict[int, int]) -> int:
        #     if i >= len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]

        #     cache[i] = max(nums[i] + memorization(i + 2, cache), memorization(i + 1, cache))

        #     return cache[i]


        # return memorization(0, {})

        def dp():
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

            return dp[-1]
        
        return dp()
