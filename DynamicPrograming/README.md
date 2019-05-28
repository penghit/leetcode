## Leetcode 121
The solution used dynamic programing skills. It keeps two numbers, maxcurr : it keeps the profit of buying the stock at a previous low
point and sell it at position i, if this value is negative, set it to 0, this means discard the previous option and try to find a new
option; maxsofar : it keeps the overall max profit seen at position i.
