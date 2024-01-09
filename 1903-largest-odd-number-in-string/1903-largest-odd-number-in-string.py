class Solution(object):
    def largestOddNumber(self, num):
        ans = ""
        for i in range(len(num)-1,-1,-1):
            if num[i]=='1' or num[i]=='3' or num[i]=='5' or num[i]=='7' or num[i]=='9':
                ans = num[:i+1]
                break            
            
        
        return ans
