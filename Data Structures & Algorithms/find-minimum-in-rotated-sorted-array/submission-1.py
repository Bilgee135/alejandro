class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R, ans = 0, len(nums) - 1, 1001

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                ans = min(ans, nums[mid])
                R = mid - 1
        
        return ans
