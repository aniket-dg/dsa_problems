class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f, s, t = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            x = set(word.lower())
            if x&f==x or x&s==x or x&t==x:
                res.append(word)
        return res