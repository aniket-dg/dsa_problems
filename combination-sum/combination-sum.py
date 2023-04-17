class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, res_here, sum_here):
            if sum_here == target:
                res.append(res_here.copy())
                return 
            
            if i >= len(candidates) or sum_here > target:
                return 
            
            res_here.append(candidates[i])
            dfs(i, res_here, sum_here+candidates[i])
            res_here.pop()
            dfs(i+1, res_here, sum_here)
        
        dfs(0, [], 0)
        return res