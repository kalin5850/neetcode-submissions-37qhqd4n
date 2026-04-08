class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        if len(s) != len(t):
            return False
        
        counter = Counter(s.lower())
        for ch in t.lower():
            counter[ch] = counter[ch] - 1
            if counter[ch] < 0:
                return False
        
        return sum(counter.values()) == 0