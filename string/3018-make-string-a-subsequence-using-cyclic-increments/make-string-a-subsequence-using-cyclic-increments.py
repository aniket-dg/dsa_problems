class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        if str2 == "":
            return True

        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            next_char = chr((ord(str1[i])-ord("a")+1)%26 + ord("a"))
            if str2[j] in [str1[i], next_char]:
                i += 1
                j += 1
            else:
                i += 1

        if j == len(str2):
            return True
        return False