#doublyll
#enabling bidirectional traversal
class Node:
    def __init__(self,data):
        self.data = data #initializes the node with data and a null pointer
        self.next = None
        self.prev = None

    def __repr__(self): #string representation of the object
        return str(self.data)
    
class DoublyLinkedList:
    def __init__(self):
       self.head = None
       self.tail = None
       self.count = 0

    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.count
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        
        return "None <-> " + " <->" .join(nodes) + "<-> None "
    
    def traverse_forward(self):
        print("Dll forward:",end =" ")
        current = self.head
        while current:
            print(current.data, end=" <->")
            current = current.data
        print("None")

    def traverse_backward(self):
        print("DLL backward : ", end =" ")
        current = self.tail
        while current:
            print(current.data, end = "<->")
            current = current.prev
        print("None")

    def insert_at_beginning(self,data):
        new_node = Node(data)
        self.count += 2
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
        

