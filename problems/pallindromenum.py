class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else :
            return x == self.reverse(x)
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return -self.reverse(-x)
        else :
            res = 0
            while x:
                res = res*10 + x%10
                x /= 10
            return res if res <= 0x7fffffff else 0