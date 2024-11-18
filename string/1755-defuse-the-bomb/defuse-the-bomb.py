class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*len(code)
        if k == 0:
            return res
            
        
        start, end = (1, k) if k > 0 else (k, -1)
        for i in range(n):
            res[i] = sum(code[(i+j)%n] for j in range(start, end+1))
        return res    