class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        arr2 = [] * (2 *n)
        i=0
        while i<2:
            for j in nums:
                arr2.append(j)
            i=i+1
        return arr2
