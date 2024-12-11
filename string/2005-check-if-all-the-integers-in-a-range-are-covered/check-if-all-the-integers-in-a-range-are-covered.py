class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        events = [0]*52
        for event in ranges:
            events[event[0]] += 1
            events[event[1]+1] -= 1
        

        max_count = 0
        for i in range(1, right+1):
            max_count += events[i]
            if i >= left and max_count == 0:
                return False
        return True