class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')        
        max_profit = float('-inf')
        
        for i in range(len(prices)):
           
            if prices[i]<buy_price:
                #buy
                buy_price = min(buy_price,prices[i])
            else:
                max_profit = max(max_profit,(prices[i]-buy_price))
                
               
        if max_profit < 0:
            return 0 
        else:
            
            return max_profit
                
        