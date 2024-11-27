class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = nums.copy()
        for i in range(1, len(nums)):
            prefix[i] = prefix[i] + prefix[i-1]
        
        def search(target):
            l, r = 0, len(prefix)-1
            res = -1
            while l <= r:
                mid = l + (r-l+1)//2
                if prefix[mid] <= target:
                    l = mid + 1
                    res = mid       
                else:
                    r = mid - 1
            return len(prefix[:res+1]) if res!= -1 else 0
        res = [search(item) for item in queries]
        return res