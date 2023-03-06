class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if k >= 26 * 26:
            return True
        d = {}
        for i in range(len(s)):
            if s[i] != t[i]:
                d[(ord(t[i]) - ord(s[i])) % 26] = d.get((ord(t[i]) - ord(s[i])) % 26, 0) + 1
        for key in d:
            if d[key] * 26 - key > k:
                return False
        return True