class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        events = []
        for num in nums:
            events.append((num[0], 1))
            events.append((num[1]+1, -1))
        
        events.sort()

        active = 0
        last_element = None
        total_points = 0
        for position, change in events:
            if active > 0 and last_element is not None:
                total_points += position - last_element
            active += change
            last_element = position
        
        return total_points