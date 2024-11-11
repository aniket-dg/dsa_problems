class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def primes(n):
            res = [0]*n
            res[0], res[1] = -1, -1
            for i in range(2, n):
                if res[i] == 0:
                    for j in range(i*i, n, i):
                        res[j] = 1
            return res
                
        max_num = max(nums)
        prime_nos_memo = primes(max_num+1)
        res = []
        prev = 0
        for item in nums:
            if item <= prev:
                return False

            for i in range(item-1, -1, -1):
                if not prime_nos_memo[i] and item - i > prev:
                    break

            prev = item - i
            
        return True