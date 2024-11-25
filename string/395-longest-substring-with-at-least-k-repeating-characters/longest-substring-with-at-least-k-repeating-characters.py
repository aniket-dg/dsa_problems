class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def search(s):
            if len(s) < k:
                return 0

            memo = Counter(s)
            for ch, count in memo.items():
                if count < k:
                    substrings = s.split(ch)
                    return max(search(substring) for substring in substrings)

            return len(s)

        return search(s)