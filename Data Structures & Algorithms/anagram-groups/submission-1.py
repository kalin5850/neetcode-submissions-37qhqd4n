

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word, key=str.lower))
            res[sorted_word].append(word)

        return list(res.values())