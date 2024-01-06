class Solution(object):
    def maxProduct(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        B =arr[::-1]
        n = len(arr)
        for i in range(1,n):
            if arr[i-1]!=0:
                arr[i] *= arr[i-1]
            
            if B[i-1]!=0:
                B[i] *= B[i-1]
            
        
        return max(arr+B)
            