class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                symbol = stack.pop()
                if ch == ')' and symbol != '(':
                    return False
                elif ch == ']' and symbol != '[':
                    return False
                elif ch == '}' and symbol != '{':
                    return False

        return len(stack) == 0