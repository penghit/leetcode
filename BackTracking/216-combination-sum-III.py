class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9 or n > 45:
            return []
        
        
        result = []
        
        def backtracking(n,k,ans,result,index):
            #print("ans:",ans," n:",n," k:",k, " index:",index)
            if n == 0 and k == 0:
                result.append(list(ans))
            if n < 0 or k < 0 or index > 9:
                return
            
            for i in range(index,10):
                ans.append(i)
                #the index passed here is (i+1), this insures that elements smaller than i will not be used again
                backtracking(n-i,k-1,ans,result,i+1)
                ans.pop()
            
        backtracking(n,k,[],result,1)
        
        return result
