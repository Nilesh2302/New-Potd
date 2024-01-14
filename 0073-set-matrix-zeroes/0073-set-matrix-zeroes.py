class Solution(object):
    def setZeroes(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        s1 = set()
        s2 = set()
        
        r = len(mat)
        c = len(mat[0])
        
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    s1.add(i)
                    s2.add(j)
        
        for i in s1:
            for j in range(c):
                mat[i][j]=0
        
        for i in range(r):
            for j in s2:
                mat[i][j]=0
                
        