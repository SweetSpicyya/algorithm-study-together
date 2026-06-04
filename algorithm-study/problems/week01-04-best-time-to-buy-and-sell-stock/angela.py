class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price = prices[0]
        profit = 0
        tmp = 0

        for i in prices:
            if price > i: 
                price = i 

            tmp = i-price 
            if profit < tmp: 
                profit = tmp
        
        if profit < 0 :
            profit = 0
        
        return profit
                
        