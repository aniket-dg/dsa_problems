class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for item in words:
            res += item.split(separator)
        return list(filter(None, res))