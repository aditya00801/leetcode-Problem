class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        to_remove = set()
        
        for i, c in enumerate(chars):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        # Any unmatched '(' left in stack must also be removed
        to_remove.update(stack)
        
        result = [c for i, c in enumerate(chars) if i not in to_remove]
        return "".join(result)