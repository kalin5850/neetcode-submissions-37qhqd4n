class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        existed = set()
        for num in nums:
            if num in existed:
                return num
            existed.add(num)