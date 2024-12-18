class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            price = prices[i]
            count = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= price:
                    count = 1
                    res.append(price-prices[j])
                    break
            if not count:
                res.append(price)
        return res