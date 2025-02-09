class Node:
    def __init__(self,data):
        self.data = data 
        self.next_node = None # reference to next data
    
class singly_linked_list:
    def __init__(self):
        self.head =  None #sll.head = None
    # traversing through the Linked List
    def traversal(self):
        current = self.head 
        if current is None:
            print("Singly Linked List is Empty")
        else:
            while current:
                print(current.data,end= " ")
                current = current.next_node
    def push(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def insert_beginning(self,data):
        new_node = Node(data)   
        new_node.next_node = self.head
        self.head = new_node  
    def insert_end(self,data):
        new_node = Node(data)
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
    def insert_sepcified(self,data,position):
        new_node = Node(data)
        current = self.head
        for i in range(1,position-1):
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node 
    def delete_at_beginning(self):
        current = self.head
        self.head = current.next_node
        current.next_node = None 
    def delete_at_end(self):
        current = self.head 
        nxt = self.head.next_node
        while nxt.next_node:
            current = current.next_node
            nxt =  current.next_node      
        current.next_node = None   
    def delete_specified(self,position):
        current = self.head
        current_next_node = current.next_node
        for i in range(1,position-1):
            current = current.next_node
            current_next_node = current_next_node.next_node
        current.next_node = current_next_node.next_node
        current_next_node = None 
    def print_nth_from_last(self,n):
        current_node = self.head 
        count = 0
        while  current_node:
            current_node = current_node.next_node
            count +=1 
        current_node = self.head 
        for i in range(1,count-n+1):
            current_node = current_node.next_node
        print("\n",current_node.data)
    def reverse(self):
        current_node = self.head 
        previous_node = None 
        while current_node:
            next_node = current_node.next_node  
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node

sll = singly_linked_list()
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
sll.push(5)
sll.push(6)

sll.traversal()
print()
#adding at the beginning
sll.insert_beginning(45)
sll.traversal()

#inserting at the end   
print()
sll.insert_end(12)
sll.traversal()

#inserting at the sepecified position
sll.insert_sepcified(23,5)
print()
sll.traversal()

sll.delete_at_beginning()
print()
sll.traversal()

sll.delete_at_end() 
print()
sll.traversal()

sll.delete_specified(3)
print()
sll.traversal()

sll.print_nth_from_last(3)
