# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #declare prev variable that the nodes will point to
        current = head #where to start, head being the first node

        while current:
            next_node = current.next #temporarily store the next node's value
            current.next = prev #assign the next value to the previous value so it points 'backward' in a sense
            prev = current #make prev the current node for the next node's iteration
            current = next_node #assign the head to the temp value that we stored the next node's value in
        return prev
