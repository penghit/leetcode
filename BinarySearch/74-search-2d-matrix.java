class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        if (nums.length == 0) return result;
        int low = 0;
        int high = nums.length - 1;
        //System.out.println(high);
        while (low + 1 < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] > target)
                high = mid - 1;
            else if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid; 
        }
        
        if (nums[low] == target) 
            result[0] = low;
        else if (nums[high] == target)
            result[0] = high;
        
        
        low = 0;
        high = nums.length - 1;
        //System.out.println(high);
        while (low + 1 < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] > target)
                high = mid - 1;
            else if (nums[mid] < target)
                low = mid + 1;
            else
                low = mid; 
        }
        
        if (nums[high] == target) 
            result[1] = high;
        else if (nums[low] == target)
            result[1] = low;
                
        
        
        return result;
    }
}
