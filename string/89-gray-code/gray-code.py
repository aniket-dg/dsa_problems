class Solution:
    def grayCode(self, n: int) -> List[int]:
        def dfs(x):
            if x=="0":
                return ["0","1"]
            if x=="1":
                return ["0"]
        
            backtrack = dfs(x[1:])
            res = []
            for item in backtrack:
                res.append("0"+item)
            for item in backtrack[::-1]:
                res.append("1"+item)
            return res
        x = "0"* n
        res = [int(item, 2) for item in dfs(x)]
        return res