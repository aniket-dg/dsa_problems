class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: x[0])
        res = []
        
        best_beauty = float("-inf")
        for i in range(len(items)):
            best_beauty = max(best_beauty, items[i][1])
            items[i][1] = best_beauty

        for query in queries:
            left, right = 0, len(items)-1
            max_beauty = 0
            while left <= right:
                mid = left + (right-left)//2
                if items[mid][0] <= query:
                    max_beauty = max(max_beauty, items[mid][1])
                    left = mid + 1
                    continue
                else:
                    right = mid - 1
                    continue

            if left == 0:
                res.append(0)
                continue
            res.append(max_beauty)

        return res