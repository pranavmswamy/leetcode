class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        # dummy elt in stack
        stack.append('#')
        
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        
        return True if stack[-1] == '#' else False
