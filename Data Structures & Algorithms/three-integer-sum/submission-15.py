class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total == 0:
                    triplets.add((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    R -= 1
 
        triplets = list(triplets)   
        return triplets
