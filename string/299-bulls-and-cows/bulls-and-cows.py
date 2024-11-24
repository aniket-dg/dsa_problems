class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        memo = Counter(secret)
        # print(memo)
        n = len(secret)
        bull = 0
        cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
                memo[guess[i]] -= 1
        # print(memo, cows)
        for i in range(n):
            if secret[i] != guess[i] and guess[i] in memo and memo[guess[i]] > 0:
                cows += 1
                memo[guess[i]] -= 1
        # print(cows)
        return f"{bull}A{cows}B"