from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        checked = [False] * len(strs)

        for i in range(len(strs)):
            if checked[i]:
                continue
            checked[i] = True
            tmp = [strs[i]]
            for j in range(i + 1, len(strs)):
                if checked[j]:
                    continue
                if Counter(strs[i].lower()) == Counter(strs[j].lower()):
                    tmp.append(strs[j])
                    checked[j] = True
            res.append(tmp)
        
        return res