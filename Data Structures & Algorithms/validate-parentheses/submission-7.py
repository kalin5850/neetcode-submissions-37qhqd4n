class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ['(', '[', '{']
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:
            if ch in open_bracket:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr != mapping.get(ch):
                    return False
        
        return len(stack) == 0
                    