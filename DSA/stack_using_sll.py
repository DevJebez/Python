class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None 
class Stack:
    def __init__(self):
        self.head = None 
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False 
    def push(self,data):
        if self.head is None:
            self.head =  Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head 
            self.head = new_node
    def pop(self):
        if self.head is None:
            return False 
        else:
            pop_node = self.head 
            self.head = pop_node.next_node
            pop_node.next_node = None 
            return pop_node.data
    def seek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        if self.isempty():
            print("Underflow Error")
        else:
            current_node = self.head 
            while current_node:
                print(current_node.data,end = " ")
                current_node = current_node.next_node
if __name__ == "__main__":
    s = Stack()
    s.push(45)
    s.push(66)
    s.push(22)
    s.push(23)
    print("Printing elements : ",end = " ")
    s.display()
    print("\npopped item : ",s.pop())
    print("Top most item :",s.seek())

    