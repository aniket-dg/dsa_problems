class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x:x[0])

        merged_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged_interval = merged_intervals[-1]

            if current_interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(current_interval[1], last_merged_interval[1])
            else:
                merged_intervals.append(current_interval)
        
        return merged_intervals