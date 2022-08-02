class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f, s, t = list("qwertyuiop"), list("asdfghjkl"), list("zxcvbnm")
        res = []
        def check(word, row):
            for item in word:
                if not item.lower() in row:
                    return False
            return True
        for word in words:
            if check(word, f):
                res.append(word)
            elif check(word, s):
                res.append(word)
            elif check(word, t):
                res.append(word)
        
        return res
        