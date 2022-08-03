class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        memo = {v: i for i, v in enumerate(list1)}
        best, ans = 1e9, []
        for idx, item in enumerate(list2):
            i = memo.get(item, 1e9)
            if i+ idx < best:
                best = i+idx
                ans = [item]
            elif i+idx == best:
                ans.append(item)
        return ans