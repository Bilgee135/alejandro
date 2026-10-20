class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * len(nums1)
        nums1Map = {x:i for i, x in enumerate(nums1)}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                nextGreater[nums1Map[stack.pop()]] = num
            if num in nums1Map:
                stack.append(num)            

        return nextGreater 
