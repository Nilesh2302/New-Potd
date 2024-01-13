class Solution(object):
    def sortColors(self,arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        m=0
        h=len(arr)-1
        
        while m<=h:
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                l+=1
                m+=1
            
            elif arr[m]==1:
                arr[l],arr[m]=arr[m],arr[l]
                m+=1
            
            elif arr[m]==2:
                arr[m],arr[h]=arr[h],arr[m]
                h-=1
            
            
                