class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def revBracket(b):
            if b == ")":
                return "("
            elif b=="]":
                return "["
            elif b == "}":
                return "{"
            return None
        
        for item in s:
            if item == "(" or item=="[" or item=="{":
                stack.append(item)
            elif item == ")" or item == "]" or item == "}":
                if not stack or not stack[-1] == revBracket(item):
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        return False
        
        