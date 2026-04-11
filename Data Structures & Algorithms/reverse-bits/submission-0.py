class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        res = 0
        
        for i in range(len(bits)):
            bits[i] = n % 2
            n = n >> 1
        
        for i in range(len(bits)):
            res += pow(2, len(bits) - 1 - i) * bits[i]
        
        return res

