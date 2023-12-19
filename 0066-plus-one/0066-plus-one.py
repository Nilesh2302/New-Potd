class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []
        n=0
        # i=0
        # while digits:
        #     temp = digits[i]%10
        #     n = n *10+temp
        #     digits //= 10
        
        for i in digits:
            n = n*10+i
        
        n +=1
        while n:
            temp = n%10
            ans.append(temp)
            n //= 10
        
        return reversed(ans)
        
        
        