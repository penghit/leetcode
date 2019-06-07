class Solution {
    
    public int findMin(int[] nums) {
        int len = nums.length;
        if (len == 1) 
            return nums[0];
        if (nums[0] < nums[len-1])
            return nums[0];
        
        int low = 0;
        int high = len - 1;
        
        while (low + 1 < high) {
            int mid = low + (high - low) / 2;
            //System.out.println(nums[mid]);
            if (nums[mid] < nums[mid-1] && nums[mid] < nums[mid+1])
                return nums[mid];
            else if (nums[mid] > nums[high])
                low = mid;
            else
                high = mid;
        }
        
        //System.out.println(low);
        //System.out.println(high);
        return nums[high];
        
    }
}
