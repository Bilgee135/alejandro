class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums) - 1):
            L, R = i + 1, len(nums) - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total == 0:
                    ans.add((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif total > 0:
                    R -= 1
                else:
                    L += 1

        return list(ans)