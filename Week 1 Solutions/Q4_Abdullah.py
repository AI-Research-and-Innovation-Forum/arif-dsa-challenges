class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        j = 2
        for i in range(2, len(nums)):
            if nums[j - 2] != nums[i]:
                nums[j] = nums[i]
                j += 1
        return j
