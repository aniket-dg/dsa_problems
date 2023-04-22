class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch.lower() in ['a','e','i','o','u']:
                vowels.append(ch)
        res = ""
        for idx, ch in enumerate(s):
            if ch.lower() in ['a','e','i','o','u']:
                res += vowels.pop()
            else:
                res += ch
        return res