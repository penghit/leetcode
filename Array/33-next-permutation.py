class Solution:
    def swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
    
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start from the end, find a number that is smaller than it's next number
        i = len(nums) - 2
        while i >=0 and nums[i+1] <= nums[i]:
            i = i - 1
        print(i)
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            print(j)
            self.swap(nums, i, j)
                
        self.reverse(nums, i+1, len(nums) - 1)
        
        

