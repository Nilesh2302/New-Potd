class Solution(object):
    def nextPermutation(self, arr):
        n = len(arr)
        if n<=2:
            return arr.reverse()
        
        pt = n-2
        while pt>=0 and arr[pt]>=arr[pt+1]:
            pt-=1
        
        if pt==-1:
            return arr.reverse()
        
        for i in range(n-1,pt,-1):
            if arr[i]>arr[pt]:
                arr[i],arr[pt]=arr[pt],arr[i]
                break
        
        arr[pt+1:] = reversed(arr[pt+1:])
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        