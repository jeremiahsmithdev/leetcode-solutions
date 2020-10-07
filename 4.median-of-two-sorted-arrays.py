class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged = nums1 + nums2
        # print(merged)
        merged = sorted(merged)
        # print(merged)
        if len(merged) % 2 == 1:
            median = merged[int(len(merged) / 2)]
            # print(median)
        else:
            median = float(
            merged[int((len(merged) / 2) - 1)] +
            merged[(int(len(merged) / 2))]
            ) / 2
            # print(median)
        return(median)



        
    print(findMedianSortedArrays(0, [1,2], [3,4]))
