class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        def get_bitmask(word):
            res = 0
            for ch in word:
                res |= (1 << ord(ch)-ord("a"))
            return res
        bit_masking = []
        for word in words:
            bit_masking.append(get_bitmask(word))

        for i in range(len(bit_masking)):
            for j in range(i+1, len(bit_masking)):
                word1, word2 = bit_masking[i], bit_masking[j]
                if word1 & word2 == 0:
                    res = max(len(words[i])*len(words[j]), res)
        return res