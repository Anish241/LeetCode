class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[1]==0:
                return 0
            return -1
        if len(nums) == 3:
            if nums[0] == nums[2]:
                return 1
            elif nums[1]+nums[2] == 0:
                return 0
            else:
                return -1
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[1:]) == 0:
                    return 0
            elif i == len(nums)-1:
                if sum(nums[:i]) == 0:
                    return i
            else:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
                
        return -1