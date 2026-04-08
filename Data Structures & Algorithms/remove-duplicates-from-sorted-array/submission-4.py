class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i, counter = 0, 0
        # for j in range(1, len(nums)):
        #     print("i: %s ==== j: %s" % (i, j))
        #     if nums[i] != nums[j]:
        #         i = j
        #         counter += 1
        #     print("counter: %s" % (counter,))
        
        # return counter + 1

        counter = 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                curr_j = nums[j]
                while j < len(nums) and curr_j == nums[j]:
                    j += 1
                nums[i + 1] = nums[j - 1]
                i += 1
                j -= 1
                counter += 1
            j += 1
        
        return counter + 1