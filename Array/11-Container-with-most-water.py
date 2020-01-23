# This method used is O(n) in time and O(1) in space
# Beginning with most left and right one, the only way to increase the volumn
# is to move the lower one towards the other side, so we continute doing this
# recording the max value encountered.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if (height[l] < height[r]):
                l = l + 1
            else:
                r = r - 1
                
        return maxarea
