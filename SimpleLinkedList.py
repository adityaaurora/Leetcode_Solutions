class Node: #make node class, this is how a new node will be made with a value and a next
    def __init__(self, val):
        self.val = val   #val value we pass
        self.next = None #initially next is none

class LinkedList:  ##class for actually making the linked list
    def __init__(self):
        self.head = None  #head is the first node of the linked list, initially none

    #insert node at the beginning 
    def insert_beg(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    #insert node at the end
    def insert_end(self, val):
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
    
    def display(self):
        if not self.head:
            print("empty linked list")
            return
        
        current = self.head
        while current:
            print(current.val, end = "-->")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_beg(4)
ll.insert_beg(25)
ll.insert_end(3)
ll.display()
