# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# concept: make a dummy node, dummy being the first node, and iterate through both lists.
# while both lists are not null, if list1 val is less than list2 val ie list1 val = 1 and list2 val = 2,
# then dummy's next node becomes list1 which is the head of the first list.
# make the list1 to list1.next so that we go through the next item in list1
# do this for the condition list2 < list1 and make list2 the next node after tail and +1 the list2
# make sure to go to the next tail node as well 
# last case is if list 1 or 2 finishes before the other, then the remaining list becomes the rest of the tail's next nodes.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
