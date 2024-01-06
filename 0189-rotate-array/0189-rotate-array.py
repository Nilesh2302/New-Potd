class Solution(object):
    def rotate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(arr)
        arr.reverse()
        s = 0
        e = k-1
        while s<=e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
            
        
        s = k
        e = len(arr)-1
        while s<=e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
            