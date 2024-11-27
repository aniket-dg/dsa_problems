class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 1
        missing = []
        while i < len(arr):
            if arr[i] == j:
                i += 1
            else:
                missing.append(j)
            j += 1

        # print(missing)
        if k <= len(missing):
            return missing[k-1]
        else:
            last_ele = max(arr[-1] if arr else 1, missing[-1] if missing else 1)
            current_missing = len(missing)
            diff = k - current_missing
            return last_ele + diff