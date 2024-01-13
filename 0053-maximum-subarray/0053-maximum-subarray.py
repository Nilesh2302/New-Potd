class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        maxi=arr[0]
        
        for i in arr:
            sum+=i
            
            maxi = max(sum,maxi)
            
            if sum<0:
                sum=0
        
        return maxi
        