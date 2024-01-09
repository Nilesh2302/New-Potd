class Solution(object):
    def getSum(self, a, b):
        ans1 = a | b
        ans2 = a & b
        return ans1+ans2
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        