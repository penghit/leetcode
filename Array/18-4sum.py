class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return
        
        res = []
        nums.sort()
        
        for p1 in range(len(nums) - 3):
            for p2 in range(p1 + 1, len(nums) - 2):
                p3 = p2 + 1
                p4 = len(nums) - 1
                
                while p3 != p4:
                    s = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    quad = [nums[p1], nums[p2], nums[p3], nums[p4]]
                    
                    if s == target:
                        if quad not in res:
                            res.append(quad)
                            
                    if s < target:
                        p3 = p3 + 1
                    else:
                        p4 = p4 - 1
                        
                        
        return res
