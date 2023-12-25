class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        small = float('inf')
        temp = float('inf')
        
        for i in nums1:
            for j in nums2:
                
                if i==j:
                    temp=i
                    if temp<small:
                        small=temp
                    continue
                
                s = i*10+j
                if s<temp:
                    temp=s
                    small=temp
                    
        for i in nums2:
            for j in nums1:                
                if i==j:
                    temp=i
                    if temp<small:
                        small=temp
                    continue
                
                s = i*10+j
                if s<temp:
                    temp=s
                    small=temp           
             
        
        return small
                
                
        