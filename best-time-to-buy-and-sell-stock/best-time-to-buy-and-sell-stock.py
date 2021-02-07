class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = float('inf')        
        max_profit = float('-inf')
        
        for p in prices:
            buy_price = min(buy_price,p)
                        
            max_profit =  max(max_profit,(p - buy_price))
        return  max_profit
            
        