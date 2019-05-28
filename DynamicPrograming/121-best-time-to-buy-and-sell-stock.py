class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxcurr = 0
        maxsofar = 0
        for i in range(1, len(prices)):
            
            maxcurr = max(0, maxcurr + prices[i] - prices[i-1])
            maxsofar = max(maxcurr, maxsofar)
            #print("i:", i, "   maxcurr:", maxcurr, "   maxsofar:", maxsofar)
            
        return maxsofar
