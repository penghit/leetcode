class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy1 = float('-inf')
        buy1 = -2**63+1
        sell1 = 0
        #buy2 = float('-inf')
        buy2 = -2**63+1
        sell2 = 0
        
        for price in prices:
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
            #print(buy1, sell1, buy2, sell2)
            
            
        return max(sell1, sell2)
