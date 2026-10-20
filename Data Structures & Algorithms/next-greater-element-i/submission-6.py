class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * len(nums1)
        nums2Map = {x:i for i, x in enumerate(nums2)}

        for i in range(len(nums1)):
            j = nums2Map[nums1[i]]
            for idx in range(j+1,len(nums2)):
                if nums2[j] < nums2[idx]:
                    nextGreater[i] = nums2[idx]
                    break

        return nextGreater 
