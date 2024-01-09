class Solution(object):
    def maxArea(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        e = len(arr)-1
        maxi = 0
        while s<=e:
            diff = e-s
            area = diff * min(arr[s],arr[e])
            
            if area>maxi:
                maxi = area
            
            if arr[s]<arr[e]:
                s+=1
            
            else:
                e -= 1
         
        return maxi
        