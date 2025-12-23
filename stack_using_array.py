class Array:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = []*capacity
        self.top = -1
    
    def is_empty(self):
        return self.top -1
    
    def is_full(self):
        return self.top == self.capacity -1
    
    def push(self,item):
        if self.is_full:
            print("stack overflow")
        self.top +=1
        self.stack[self.top] = item
        print("pushed an item to stack successfully")

    def pop(self,item):
        if self.is_empty:
            print("stack underflow")
        self.top -= 1
        item = self.stack[self.top]
        print("pop an item successfully")
        return item
    
    def size(self):
        return self.top + 1 
    
array  = Array(5)
array.push(10) 
array.push(20)
array.push(30)
print(f"Current stack size: {array.size()}")
array.pop(None)
print(f"Current stack size after pop: {array.size()}")
print("Arithematic Module Loaded Successfully")

        









        
