class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1

        while L <= R:
            mid = L + (R - L) // 2
            val = matrix[mid // n][mid % n]

            if target > val:
                L = mid + 1
            elif target < val:
                R = mid - 1
            else:
                return True
        
        return False
