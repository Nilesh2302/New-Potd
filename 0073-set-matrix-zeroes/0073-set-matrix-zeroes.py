class Solution(object):
    def setZeroes(self, arr):
        
        #t.c : O(mn) and s.c. is O(m+n)
        
        m = len(arr)
        n = len(arr[0])
        
        r = set()
        c = set()
        
        for i in range(m):
            for j in range(n):
                if arr[i][j]==0:
                    r.add(i)
                    c.add(j)
        
        #make row with 0
        for i in r:
            for j in range(n):
                arr[i][j]=0
        
        #make column with 0
        for i in range(m):
            for j in c:
                arr[i][j]=0
        
        return arr
        


          
                        