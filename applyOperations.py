class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        be = []
        ce = []
        ke = []

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            ke.append(nums[i])

        for j in ke:
            if j != 0:
                be.append(j)
            else:
                ce.append(j)

        be.extend(ce)
        return be
