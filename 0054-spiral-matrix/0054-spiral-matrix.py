class Solution(object):
    def spiralOrder(self, arr):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        r = len(arr)
        c = len(arr[0])
        strow = 0
        stcol = 0
        enrow = r-1
        encol = c-1
        
        cnt = 0
        ans = []
        
        while cnt<r*c:
            
            i=stcol
            while i<=encol and cnt<r*c:
                ans.append(arr[strow][i])
                i+=1
                cnt+=1
            
            strow+=1
            
            i = strow
            while i<=enrow and cnt<r*c:
                ans.append(arr[i][encol])
                i+=1
                cnt+=1
            
            
            encol-=1
            i = encol
            while i>=stcol and cnt<r*c:
                ans.append(arr[enrow][i])
                i-=1
                cnt+=1
            
            enrow-=1
            
            i = enrow
            while i>=strow and cnt<r*c:
                ans.append(arr[i][stcol])
                i-=1
                cnt+=1
            
            stcol+=1
            
            
            
                
        
        
        
        return ans
                
            
        
            
            
        