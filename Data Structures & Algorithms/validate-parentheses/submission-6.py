class Solution:
    def isValid(self, s: str) -> bool:
        characters = ['(', '{', '[']

        #use a stack
        stack = []

        for i in s:
            if i in characters:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                elif i == '}' and stack[-1] != '{':
                    return False
                elif i == ']' and stack[-1] != '[':
                    return False
                stack.pop()
            
        
        if len(stack) == 0: return True
        else: return False
