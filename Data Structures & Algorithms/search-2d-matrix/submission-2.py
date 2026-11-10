class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = False

        for row in matrix:
            if target > row[-1]:
                continue

            L, R = 0, len(row) - 1
            while L <= R:
                mid = L + (R - L) // 2

                if target > row[mid]:
                    L = mid + 1
                elif target < row[mid]:
                    R = mid - 1
                else:
                    ans = True
                    break
        return ans
