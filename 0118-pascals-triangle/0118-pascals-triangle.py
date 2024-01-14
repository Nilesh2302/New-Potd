class Solution(object):
    def generate(self, n):
        ans = [[1]]
        
        for i in range(1,n):
            temp = [1]
            ind = 0
            while i!=1:
                temp.append(ans[-1][ind]+ans[-1][ind+1])
                ind+=1
                i-=1
            
            temp.append(1)
            ans.append(temp)
        
        return ans
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        