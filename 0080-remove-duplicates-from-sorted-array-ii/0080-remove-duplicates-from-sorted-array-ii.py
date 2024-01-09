class Solution(object):
    def removeDuplicates(self, arr):
        count = {}
        ans = []
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            # Add the number only if it appears the first or second time
            if count[num] <= 2:
                ans.append(num)
        
        arr[:] = ans[:]
        return len(ans)

