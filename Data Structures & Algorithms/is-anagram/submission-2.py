class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        if len(s) != len(t):
            return False
        
        counter_s = Counter(s.lower())
        counter_t = Counter(t.lower())

        return counter_s == counter_t