# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        left_idx, right_idx = 0, 0
        result = []
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx].key <= right[right_idx].key:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        while left_idx < len(left):
            result.append(left[left_idx])
            left_idx += 1
        while right_idx < len(right):
            result.append(right[right_idx])
            right_idx += 1
        
        return result

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        middle = len(pairs) // 2
        left = self.mergeSort(pairs[0:middle])
        right = self.mergeSort(pairs[middle:len(pairs)])

        return self.merge(left, right)
