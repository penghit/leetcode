class Solution {
    public int findPeakElement(int[] nums) {
        int len = nums.length;
        if (len == 0) return -1;
        if (len == 1) return 0;
        
        if (nums[0] > nums[1]) return 0;
        if (nums[len-1] > nums[len-2]) return len-1;
        
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
}
