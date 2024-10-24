class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        res = []
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                print(f"{top}{i}")
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom+1):
                print(f"{i}{right}")
                res.append(matrix[i][right])
                
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    print(f"{bottom}{i}")
                    res.append(matrix[bottom][i])
                    
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    print(f"{i}{left}")
                    res.append(matrix[i][left])
                    
                left += 1
        
        return res 