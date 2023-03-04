# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            elif x == ')':
                if len(stack) == 0 or stack.pop() != '(': return False
            elif x == ']':
                if len(stack) == 0 or stack.pop() != '[': return False
            elif x == '}':
                if len(stack) == 0 or stack.pop() != '{': return False
        
        return len(stack) == 0