class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        INT_NUM1 = 0
        INT_NUM2 = 0
        idx1 = 0
        idx2 = 0
        while idx1 < len(num1):
            INT_NUM1 = INT_NUM1 * 10 + (ord(num1[idx1]) - ord('0'))
            idx1 += 1
        while idx2 < len(num2):
            INT_NUM2 = INT_NUM2 * 10 + (ord(num2[idx2]) - ord('0'))
            idx2 += 1
        result = INT_NUM1 + INT_NUM2
        return str(result)