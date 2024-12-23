class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j - 1

            return True
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res