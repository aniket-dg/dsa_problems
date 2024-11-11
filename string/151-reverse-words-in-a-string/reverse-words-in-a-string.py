class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        return " ".join(s.strip().split(" ")[::-1])