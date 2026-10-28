class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        l, r = 0, 0

        while l < len(nums) - 1:
            while r + 1 < len(nums) and nums[r + 1] == nums[l]:
                r += 1

            while l != r:
                nums.remove(nums[r])
                r -= 1
            
            l += 1
            r += 1

        return len(nums)
        
