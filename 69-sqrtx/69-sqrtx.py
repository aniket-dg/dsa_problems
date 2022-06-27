class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        start, end = 1, x//2
        
        while start < end:
            mid = (start + (end-start)//2) + 1
            midS = x // mid
            
            if mid == midS:
                return mid
            
            if midS < mid:
                end = mid - 1
            
            else:
                start = mid
        
        return start
    
        
    
