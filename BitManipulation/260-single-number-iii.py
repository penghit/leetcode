class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = {}
        c=[]
        for x in nums:
            if x not in seen:
                seen[x] = 1
            else:
                if(seen[x]==1):
                    seen[x]+=1
        
        for x in set(nums):
            if(seen[x]==1):
                c.append(x)
        return c       
