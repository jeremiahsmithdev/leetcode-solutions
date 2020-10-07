class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        xindex = 0
        for x in nums:
            # get index
            yindex = 0
            for y in nums:
                if yindex is not xindex:
                    if x + y == target:
                        return (xindex, yindex)
                yindex += 1
            xindex += 1
