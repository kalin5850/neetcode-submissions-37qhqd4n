class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] != val:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        idx = 1
        for i in range(len(nums)):
            if nums[i] == val:
                idx = i
                break
            idx += 1
        return idx
