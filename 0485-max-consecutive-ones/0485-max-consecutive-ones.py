class Solution(object):
    def findMaxConsecutiveOnes(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        maxcnt=0
        for i in arr:
            if i==1:
                cnt+=1
                maxcnt = max(cnt,maxcnt)
            
            else:
                cnt=0
        
        return maxcnt
        