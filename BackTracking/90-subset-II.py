class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        
        nums.sort()
        i=0
        while i < len(nums):
            count = 0
            while (count + i) < len(nums) and nums[count + i] == nums[i]:
                count = count + 1
            previousN = len(result)
            for j in range(0, previousN):
                for k in range(count):
                    result.append(result[j]+[nums[i]]*(k+1))
            
            i = i + count
        
        return result
