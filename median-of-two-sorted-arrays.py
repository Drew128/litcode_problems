class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = sorted(nums1+nums2)
        length = len(array)
        if length%2 == 1:
            return array[int(length/2)]
        else:
            half = int(length/2)
            return (array[half-1] + array[half]) / 2
