class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 if flowerbed[0] else 1
    
        for item in flowerbed:
            if item:
                p = int((count-1)/2)
                n -= p
                count = 0
            else:
                count += 1
        n -= count // 2
        return n <= 0