class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for idx, i in enumerate(s):
            if counter[i] == 1:
                return idx
        
        return -1