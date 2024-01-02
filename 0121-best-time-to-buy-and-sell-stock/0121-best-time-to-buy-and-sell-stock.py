class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_p = prices[0]
        p = 0
        
        for i in range(1,len(prices)):
            if prices[i]<min_p:
                min_p = prices[i]
            
            else:
                p = max(p,prices[i]-min_p)
         
        return p
          
    