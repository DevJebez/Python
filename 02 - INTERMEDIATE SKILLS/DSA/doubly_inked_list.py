class Node:
    def __init__(self,data):
        self.data =  data 
        self.next_node = None 
        self.previous_node = None
class Doubly_linked_list:
    def __init__(self):
        self.head = None
    
    def traversal_forward(self):
        print()
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data ,end = " ")
                current_node = current_node.next_node
    def traversal_back(self):
        print()
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            while current_node:
                print(current_node.data,end = " ")
                current_node = current_node.previous_node
    def insert_beginning(self,data):
        new_node = Node(data)
        current_node = self.head 
        current_node.previous_node = new_node
        new_node.next_node = current_node 
        self.head = new_node
    def insert_end(self,data):
        new_node = Node(data)
        current_node = self.head 
        while current_node.next_node:
            current_node = current_node.next_node
        new_node.previous_node = current_node
        current_node.next_node = new_node
    def insert_sepcified(self,data,position):
        if position == 1:
            dll.insert_beginning(data)
        else:
            new_node = Node(data)
            current_node = self.head 
            for i in range(1,position-1):
                current_node = current_node.next_node
                new_node.previous_node = current_node
            new_node.next_node = current_node.next_node
            current_node.next_node.previous_node = new_node
            current_node.next_node=new_node        
    def delete_at_beginning(self):
        current_node =  self.head
        self.head = current_node.next_node
        current_node.previous_node = None 
    def delete_at_end(self):
        current_node =  self.head 
        while current_node.next_node:
            current_node = current_node.next_node 
        print()
        print(current_node.previous_node.next_node)#<__main__.Node object at 0x00000220BA95FBE0>
        print(current_node.previous_node)#<__main__.Node object at 0x0000024112EAFCD0>
        current_node.previous_node.next_node= None
    def delete_specified(self,position):
        if position == 1:
            pass 
        else:
            current_node= self.head 
            for i in range(1,position):
                current_node = current_node.next_node
            current_node.next_node.previous_node = current_node.previous_node 
            current_node.previous_node.next_node = current_node.next_node 

        

n1 = Node(2)
dll = Doubly_linked_list()
dll.head = n1
n2 = Node(3)
n2.previous_node = n1
n1.next_node = n2
n3 = Node(4)
n3.previous_node = n2
n2.next_node = n3
n4 = Node(5)
n4.previous_node = n3
n3.next_node = n4


dll.traversal_forward()

dll.traversal_back()

dll.insert_beginning(888)

dll.traversal_forward()

dll.insert_end(23)

dll.traversal_forward()

dll.insert_sepcified(333,4)

dll.traversal_forward()

dll.delete_at_beginning()
dll.traversal_forward()

dll.delete_at_end()
dll.traversal_forward()

dll.delete_specified(3)
dll.traversal_forward()

print()

print(n2.previous_node.next_node)
print(n1.next_node)