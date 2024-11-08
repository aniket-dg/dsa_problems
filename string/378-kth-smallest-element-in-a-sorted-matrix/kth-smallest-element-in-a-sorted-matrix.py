class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def calculate_element(matrix, num):
            res = 0
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] <= num:
                        res += 1
                    else:
                        break
            return res

        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        while low < high:
            mid = (low + high)//2
            
            total_elements = calculate_element(matrix, mid)
            if total_elements < k:
                low = mid + 1
            else:
                high = mid
        return low
            
        
    