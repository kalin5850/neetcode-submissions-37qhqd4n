class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ Brute force """
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         continue
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] != nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             break
        # idx = 1
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         idx = i
        #         break
        #     idx += 1
        # return idx

        """ Optimized """
        i, j = 0, len(nums) - 1
        while i <= j:
            while i < len(nums):
                if nums[i] == val:
                    break
                i += 1
            while j >= 0:
                if nums[j] != val:
                    break
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        print(nums)
        return j + 1


