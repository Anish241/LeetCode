class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        for i in range(len(digits)):
            if i == 0:
                for j in range(len(d[digits[i]])):
                    res.append(d[digits[i]][j])
            else:
                temp = []
                for j in range(len(d[digits[i]])):
                    for k in range(len(res)):
                        temp.append(res[k] + d[digits[i]][j])
                res = temp
        return res