class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, number in enumerate(nums):
            remaining = target - number
            if remaining in table:
                return [table.get(remaining), idx]
            else:
                table[number] = idx