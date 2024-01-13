class Solution(object):
    def twoSum(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}
        for i in range(len(arr)):
            temp = target-arr[i]
            if temp in d:
                return [d[temp],i]
            
            else:
                d[arr[i]] = i
                
                
        