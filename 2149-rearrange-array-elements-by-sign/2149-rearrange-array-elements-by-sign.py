class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        p = []
        n = []
        
        for i in nums:
            if i<0:
                n.append(i)
            
            else:
                p.append(i)
        
        ans = []
        for i in range(len(p)):
            ans.append(p[i])
            ans.append(n[i])
        
        return ans