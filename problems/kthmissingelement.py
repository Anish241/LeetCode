
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = 1
        while i < len(arr):
            if arr[i] != j:
                k -= 1
                if k == 0:
                    return j
            else:
                i += 1
            j += 1
        return arr[-1] + k