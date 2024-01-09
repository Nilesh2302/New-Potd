class Solution(object):
    def removeDuplicates(self,arr):
        d = dict({})
        ans = []
        for i in arr:
            if i in d:
                d[i] += 1
            
            else:
                d[i] = 1
            
            if d[i]<=2:
                ans.append(i)
        
        
        arr[:] = ans[:]
        return len(ans)
