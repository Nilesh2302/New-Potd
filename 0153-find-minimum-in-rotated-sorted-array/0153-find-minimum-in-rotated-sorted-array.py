class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = len(arr)-1
        
        while s<e:
            mid = s + (e-s)//2
            if arr[mid]<arr[e]:
                e = mid
            
            elif arr[mid]>arr[e]:
                s = mid+1
             
            else:
                e = mid-1
         
        return arr[s]