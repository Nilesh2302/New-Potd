class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        small = float('inf')
        
        for i in nums1:
            for j in nums2:
                
                if i==j:
                    if i<small:
                        small=i
                        continue
                
                temp = i*10+j
                if temp<small:
                    small = temp
        
        for i in nums2:
            for j in nums1:
                
                if i==j:
                    if i<small:
                        small=i
                        continue
                
                temp = i*10+j
                if temp<small:
                    small = temp
                   
                    
                  
             
        
        return small
                
                
        