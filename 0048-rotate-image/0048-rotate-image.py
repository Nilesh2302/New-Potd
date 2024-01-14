class Solution(object):
    def rotate(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(mat)):
            for j in range(i):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        
        for i in mat:
            i.reverse()
            