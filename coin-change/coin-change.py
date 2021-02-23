class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        amounts = [float('inf')]*(amount+1)
        
        amounts[0] = 0
        
        for c in coins:
            for j in range(c,amount+1):
                
                amounts[j] = min(amounts[j], amounts[j-c]+1)
        
        if amounts[amount] == float('inf'):
            return -1
        return amounts[amount]
            
        
  