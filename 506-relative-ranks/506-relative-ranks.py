class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        position = sorted(score, reverse=True)
        # position.sort(reverse=True) 
        res = []
        for i,item in enumerate(score):
            pos = position.index(item) + 1
            # print(pos)
            if pos == 1:
                res.append("Gold Medal")
            elif pos==2:
                res.append("Silver Medal")
            elif pos==3:
                res.append("Bronze Medal")
            else:
                res.append(str(pos))
        
        return res