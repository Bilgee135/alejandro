class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True
        return False
        