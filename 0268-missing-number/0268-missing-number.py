class Solution(object):
    def missingNumber(self, arr):
        N = len(arr)
        total = N*(N+1)//2
        
        return total - sum(arr)
        """
        :type nums: List[int]
        :rtype: int
        """
        