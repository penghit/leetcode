class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ans = [0 for i in range(1+num)]
        #print(ans)
        
        i = 0
        b = 1
        
        while (b <= num):
            while (i < b and i + b <= num):
                ans[i + b] = ans[i] + 1
                i = i + 1
            
            i=0
            b = b*2
        
        return ans
