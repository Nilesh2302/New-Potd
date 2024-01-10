from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        s1 = Counter(s)
        t1 = Counter(t)
        
        if s1==t1:
            return True
        
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        