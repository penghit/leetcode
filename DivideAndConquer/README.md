# This folder contains problems that can be dealt with divide and conquer method

# Leetcode 23
The easiest way to solve this problem is just to loop over all the nodes and keep the numbers appearing in a list, and then sort the list,
then creating a new ListNode, loop over the sorted list and add the sorted numbers to the new ListNode and return the ListNode.
The complexity would be O(NlogN), and space complexity would be O(N).

# Leetcode 395
Thoughts:The problems wants to us to return the longest substring with characters which repeats at least K times. So we can know that the characters appears less than K time must not be in the substring, so we can separate the total string with the characters appears less than K times, and find the longest string in the separated sub strings. Which can be achieved by recursive calls.
