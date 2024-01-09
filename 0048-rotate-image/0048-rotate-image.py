class Solution(object):
    def rotate(self, arr):
        r = len(arr)
        c = len(arr[0])
        
        for i in range(r):
            for j in range(i):
                    arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
        
        for i in arr:
            i.reverse()
        
        
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        