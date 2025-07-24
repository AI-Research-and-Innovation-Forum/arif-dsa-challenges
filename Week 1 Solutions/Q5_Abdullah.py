class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=nums[0]
        count = 1
        for i in nums[1:]:
            count += (1 if current == i else -1)
            if not count:
                current = i
                count = 1
        return current 
