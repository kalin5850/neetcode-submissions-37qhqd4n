# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def quick_sort(arr: list[Pair], start: int, end: int) -> list[Pair]:
            if end - start + 1 <= 1:
                return arr
            pivot = arr[end]
            swap_idx = start
            for i in range(start, end):
                if arr[i].key < pivot.key:
                    arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
                    swap_idx += 1
            arr[swap_idx], arr[end] = arr[end], arr[swap_idx]
            quick_sort(arr, start, swap_idx - 1)
            quick_sort(arr, swap_idx + 1, end)

            return arr

        return quick_sort(pairs, 0, len(pairs) - 1)