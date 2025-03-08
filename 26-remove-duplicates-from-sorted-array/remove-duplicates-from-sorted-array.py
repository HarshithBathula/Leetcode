class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        unique = True

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                unique = True;
            elif nums[i] == nums[i-1]:
                unique = False;
            if unique:
                nums[j+1] = nums[i];
                j = j+1;
        return j+1        