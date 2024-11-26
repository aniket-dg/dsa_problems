class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        def search(nums, k):
            print(nums, k)
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l+1)//2
                if nums[mid] == k:
                    return True
                elif nums[mid] > k:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        for i in range(len(arr)):
            if arr[i] < 0:
                if search(arr[:i], arr[i]*2):
                    return True
            elif search(arr[i+1:], arr[i]*2):
                return True
        return False