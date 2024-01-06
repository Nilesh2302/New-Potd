class Solution(object):
    def moveZeroes(self, arr):
        i = 0
        for j in range(len(arr)):
            if arr[j]==0:
                continue
            
            else:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                
                
        
    
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        