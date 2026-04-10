class Solution:
    def hammingWeight(self, n: int) -> int:
        remainder, quotient = 0, n
        count = 0

        while quotient > 1:
            remainder = quotient % 2
            quotient //= 2
            if remainder == 1:
                count += 1
        if quotient == 1:
            count += 1

        return count