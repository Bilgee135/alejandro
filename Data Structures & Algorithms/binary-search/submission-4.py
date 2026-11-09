class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            # Why this formula is better?
            # M = L + (R - L) // 2
            M = (L + R) // 2
            if target > nums[M]:
                L += 1
            elif target < nums[M]:
                R -= 1
            else:
                return M
        return -1