class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [-1 for i in range(amount+1)]
        print(ans)
        
        ans[0] = 0
        for i in range(1,len(ans)):
            for coin in coins:
                if i - coin < 0:
                    continue
                if ans[i-coin] > -1:
                    if ans[i] == -1:
                        ans[i] = ans[i-coin] + 1
                    else:
                        ans[i] = min(ans[i], ans[i-coin]+1)
        
        
        return ans[-1]
