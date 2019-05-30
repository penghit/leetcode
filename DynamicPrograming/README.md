## Leetcode 121
The solution used dynamic programing skills. It keeps two numbers, maxcurr : it keeps the profit of buying the stock at a previous low
point and sell it at position i, if this value is negative, set it to 0, this means discard the previous option and try to find a new
option; maxsofar : it keeps the overall max profit seen at position i.


## Leetcode 122
The idea is simple : when we saw a valley (price lower than both sides), we buy the stock, and sell the stock at the day whose
next day is going to fall.


## Leetcode 123
* buy1 keeps the max profit when buying the first time at position i,
* sell1 keeps the max profit when selling the first transaction at position i,
* buy2 keeps the max profit when buying the second time at position i,
* sell2 keeps the max profit when selling the second transaction at position i.

sells2 at position i is equal to the max(sell2 at position i-1, buy2 at position i-1 plus price at position i), which means that if sell
the stock at position i-1 is higher than selling at i, we will keep the decision that sell at position i-1, otherwise, we should change
the mind and sell at position i instead of i-1.

buy2, sell1 and buy1 can be analysed the same way


## Leetcode
The idea is to keep a list of the minimum of coins needed to make up the amount from 1 to amount.

Let's say we have three kind of coins[1, 2, 5] and the amount is 11, then ans[1] should be 1, since one 1 coin is enough. And
ans[2] should be 1, since one 2 coin is enough. ans[3] should be min(ans[3-1]+1, ans[3-2]+1, ans[3-5]+1) (if the value exists), 
the meaning is that we should consider wether the one or more of the previous amount plus one of the coins can make up 3. If there
are multiple, we choose the smallest one.
