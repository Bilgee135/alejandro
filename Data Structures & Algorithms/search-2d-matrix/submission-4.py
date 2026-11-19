class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        L, R = 0, r*c - 1

        while L <= R:
            mid = (L + R) // 2
            val = matrix[mid // c][mid % c]
            
            if val > target:
                R = mid - 1
            elif val < target:
                L = mid + 1
            else:
                return True
            
        return False