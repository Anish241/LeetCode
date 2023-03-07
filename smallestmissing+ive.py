class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        while nums and nums[0] <= 0:
            nums.pop(0)
        
        
        if not nums:
            return 1
        if nums[0] > 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i-1] + 1
        return nums[-1] + 1
    

              

        