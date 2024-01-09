class Solution(object):
    def longestCommonPrefix(self, strs):
        ans=""
        temp1 = max(strs)
        temp2 = min(strs)
        ans = ""
        
        l = len(temp2)
        
        for i in range(l):
            if temp1[i]==temp2[i]:
                ans+=temp1[i]
            else:
                break
        
        return ans
        """
        :type strs: List[str]
        :rtype: str
        """
        