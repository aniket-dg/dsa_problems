class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        return len(Counter(ransomNote)-Counter(magazine)) == 0