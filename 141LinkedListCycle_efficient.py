# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# uses tortoise and hare method, where both pointers point to the first node, and the hare moves faster than the tortoise. 
# Make the hare traverse 2 nodes and make tort traverse one node at once while hare, tort and hare.next is true. 
# Return true if they are equal to each other because they will meet at least once if the list is in a cycle


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort = head
        hare = head

        while tort and hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
                return True
        return False

#this can be done through a set as well, make an empty set, and add elements of the list to it. 
# if the element is in the set then return True
