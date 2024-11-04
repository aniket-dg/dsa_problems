class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        i = 0
        while i < len(word):
            res_here = 1
            while i+1 < len(word) and word[i] == word[i+1] and res_here < 9:
                res_here += 1
                i += 1
            res += f"{res_here}{word[i]}"
            i += 1
        return res