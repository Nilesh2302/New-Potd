class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        e=len(arr)-1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]==target:
                return mid

            elif target>arr[mid]:
                s = mid+1

            else:
                e = mid-1

        return -1                

