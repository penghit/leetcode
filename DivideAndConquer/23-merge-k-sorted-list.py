# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # create a list to store all the elements in the node
        numlist = []
        
        #loop over the list to store the elements in numlist
        for node in lists:
            while node:
                numlist.append(node.val)
                node = node.next
        
        # sort the list
        numlist.sort()
        #print(numlist)
        
        # create a new list to store the result
        head = curr = ListNode(0)
        for num in numlist:
            curr.next = ListNode(num)
            curr = curr.next
        
        return head.next
