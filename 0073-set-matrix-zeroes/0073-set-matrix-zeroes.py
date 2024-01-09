class Solution(object):
    def setZeroes(self, arr):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(arr)
        m = len(arr[0])
        
        s1 = set()
        s2 = set()
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    s1.add(i)
                    s2.add(j)
        
        for i in s1:
            for j in range(m):
                arr[i][j]=0
        
        
        for i in range(n):
            for j in s2:
                arr[i][j]=0
                