class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        
        arr2.sort()
        for i in arr1:
            index = bisect.bisect_left(arr2, i)
            min_dist = float('inf')
            if index > 0:
                min_dist = min(min_dist, abs(i-arr2[index-1]))
            if index < len(arr2):
                min_dist = min(min_dist, abs(i-arr2[index]))
            if min_dist > d:
                res += 1
        return res