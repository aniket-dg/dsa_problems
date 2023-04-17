class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return 0
        
        res = ["1"]
        
        for i in range(1, n):
            prev = res[i-1]
            count = 1
            say = ""
            for j in range(1, len(prev)):
                if prev[j] == prev[j-1]:
                    count += 1
                else:
                    say += f"{count}{prev[j-1]}"
                    count = 1
            
            say += f"{count}{prev[-1]}"
            res.append(say)
        
        return res[-1]