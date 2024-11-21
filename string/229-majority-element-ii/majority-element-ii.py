class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = len(nums)//3
        nums_counter = Counter(nums)

        res = []
        for k, v in nums_counter.items():
            if v > counter:
                res.append(k)
        
        return res