class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            
            else:
                d[i] = 1
        
        for i in d:
            if d[i]>1:
                return True
        
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        