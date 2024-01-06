class Solution(object):
    def findMin(self, nums):
        s = 0
        e = len(nums)-1
        while s<e : 
            mid = s + (e-s)//2
            if nums[mid]<nums[e]:   #mid < end
                e   =mid
            
            elif nums[mid]>nums[e]:  # mid > end
                s = mid + 1
            
            elif nums[mid]==nums[e]:                   #mid==end
                e = mid - 1
                  
        return nums[s]  
        