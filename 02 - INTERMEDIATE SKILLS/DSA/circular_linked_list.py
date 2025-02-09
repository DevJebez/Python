class Node:
    def __init__(self,data):
        self.next_node = None 
        self.data = data 
class cricular_linked_list:
    def __init__(self):
        self.head = None 
    def push(self,data):
        new_node = Node(data)
        new_node.next_node = self.head 
        if self.head != None:
            current_node = self.head 
            while current_node.next_node  != self.head:
                current_node = current_node.next_node 
            current_node.next_node =  new_node
        else:
            #print("Adding first element")
            new_node.next_node = new_node
        self.head = new_node     
    def traversal(self):
        print()
        current_node = self.head
        while current_node.next_node  != self.head:
            print(current_node.data,end = " ")
            current_node = current_node.next_node
        print(current_node.data)
    def traversal_recur(self,temp = None):
        if temp == None:
            temp = self.head 
        if temp.next_node == self.head:
            print(temp.data,end =  " ")
            return
        print(temp.data,end = " ")
        self.traversal_recur(temp.next_node)
    def delete(self,pos = None):
        temp = self.head 
        cur_next = temp.next_node
        while temp.next_node:
            temp = temp.next_node
        temp.next_node = self.head.next_node
        self.head = cur_next
            
cll = cricular_linked_list()
cll.push(5)
cll.push(4)
cll.push(3)
cll.push(2)
cll.push(1)
cll.traversal()
print("Traversing a cirucular linked list using recursion")
cll.traversal_recur()

print("\nDeleting an element")
cll.delete(3)
cll.traversal()
