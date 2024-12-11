class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sweep line algorithm
        events = []
        for num in nums:
            events.append((num-k, 1))
            events.append((num+k+1, -1))
        
        events.sort()
        curr_beauty = 0
        max_beauty = 0
        for value, effect in events:
            curr_beauty += effect
            max_beauty = max(max_beauty, curr_beauty)
        
        return max_beauty