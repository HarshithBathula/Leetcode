class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                nums[j+1] = nums[i];
                j = j+1;
        return j+1        