class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(pos, res_here, sum_here):
            if sum_here == 0:
                res.append(res_here.copy())
            
            if sum_here <= 0:
                return 
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                res_here.append(candidates[i])
                dfs(i+1, res_here, sum_here - candidates[i])
                res_here.pop()
                prev = candidates[i]
        
        dfs(0, [], target)
        return res