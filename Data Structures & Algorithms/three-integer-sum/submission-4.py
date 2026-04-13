class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        nums.sort()
        print(nums)
        for idx, target in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -target:
                    l += 1
                elif nums[l] + nums[r] > -target:
                    r -= 1
                else:
                    if (target, nums[l], nums[r]) not in visited:
                        res.append([target, nums[l], nums[r]])
                        visited.add((target, nums[l], nums[r]))
                    r -= 1

        return res