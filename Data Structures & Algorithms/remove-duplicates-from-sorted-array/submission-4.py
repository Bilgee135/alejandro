class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0

        while R < len(nums):
            if nums[R] == nums[L]:
                R += 1
            else:
                L += 1
                nums[L] = nums[R]

        return L + 1
        
