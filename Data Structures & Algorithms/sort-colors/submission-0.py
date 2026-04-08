class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket: list[int] = [0, 0, 0]
        for num in nums:
            bucket[num] += 1
        j = 0
        for i in range(len(bucket)):
            for count in range(bucket[i]):
                nums[j] = i
                j += 1   