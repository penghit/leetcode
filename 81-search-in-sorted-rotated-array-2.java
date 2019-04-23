class Solution {
    
    private int findPeakElement(int[] nums) {
        int len = nums.length;
        if (len == 0) return -1;
        if (len == 1) return 0;
        
        
        int low = 0;
        int high = len - 1;
        
        while (low + 1 < high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1])
                return mid;
            else if (nums[mid] > nums[mid+1] && nums[mid] < nums[mid-1])
                high = mid;
            else if (nums[mid] < nums[mid+1] && nums[mid] > nums[mid-1])
                low = mid;
            else
                high = mid;
        }
        
        return -1;
    }    
    
    
    private boolean binarySearch(int[] nums, int target, int left, int right) {
        if (left > right)
            return false;
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target)
            return true;
        else if (nums[mid] < target)
            return binarySearch(nums, target, mid+1, right);
        else
            return binarySearch(nums, target, left, mid-1);
    }
    
    
    public boolean search(int[] nums, int target) {
        int peakelement = findPeakElement(nums);
        
        int len = nums.length;
        if (peakelement == -1) {
            for (int i=0; i<len; i++) {
                if (nums[i] == target)
                    return true;
            }
            return false;
        }
    
        System.out.println(peakelement);
        
        if (peakelement == len - 1)
            return binarySearch(nums, target, 0, len - 1);
        else
            return (binarySearch(nums,target, 0, peakelement) || binarySearch(nums, target, peakelement + 1, len - 1));
        
        
    
    
    }
        
}
