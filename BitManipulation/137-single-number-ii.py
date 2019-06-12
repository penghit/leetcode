class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        
        for value in nums:
            print('before changing:')
            print('one:', one)
            print('two:', two)
            one = one ^ value & (~two)
            two = two ^ value & (~one)
            print('after changing:')
            print('one:', one)
            print('two:', two)          
            
        return one
