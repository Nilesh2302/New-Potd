class Solution(object):
    def rotateString(self, s, goal):
        
        if len(s)!=len(goal):
            return False
        
        goal += goal
        if s in goal:
            return True
        
        return False
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        