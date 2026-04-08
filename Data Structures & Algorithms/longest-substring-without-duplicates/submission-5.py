class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            window = set()
            for j in range(i, len(s)):
                if s[j] in window:
                    break
                window.add(s[j])
            length = max(length, len(window))

        return length