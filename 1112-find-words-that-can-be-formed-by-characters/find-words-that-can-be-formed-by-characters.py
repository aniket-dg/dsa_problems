class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        memo = Counter(chars)
        res = 0
        for word in words:
            word_counter = Counter(word)
            bit = True
            for k, v in word_counter.items():
                if memo[k] < v:
                    bit = False
            if bit:
                res += len(word)
        return res