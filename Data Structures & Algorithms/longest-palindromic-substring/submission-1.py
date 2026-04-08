class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force
        ''' start, end = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l <= r and s[l] == s[r]:
                    if (r - l + 1) >= (end - start + 1):
                        start, end = l, r
                    l += 1
                    r -= 1
        
        return s[start: end + 1] '''

        # Improved
        start, end = 0, 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >= (end - start + 1):
                    start, end = l, r
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >= (end - start + 1):
                    start, end = l, r
                l -= 1
                r += 1
        
        return s[start:end+1]

