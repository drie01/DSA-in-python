#stack class 
class Stack:
    def __init__(self):
        #this list will act like our stack
        self.elements = []
    
    def is_empty(self):
        #stack is empty when list has no items
        return len(self.elements) == 0
    
    def push(self, value):
        #push basically means adding to the end
        self.elements.append(value)
    
    def pop(self):
        #pop from end, but only if non-empty
        if not self.is_empty():
            return self.elements.pop()
        return None
    
    def peek(self):
        #peek means “show me the top element but don’t remove it”
        if not self.is_empty():
            return self.elements[-1]
        return None

    def infix_to_postfix(self,expression):
        precendence = {'+': 1, '-' :1, '*' : 2, '/':2,'^':3}
        output = []
        operation_stack = []
        tokens = expression.split()
        for token in tokens:
            if token.isalnum():
                output.append(token)

            elif token in "(":
                operation_stack.append(token)

            elif token in ")":
                while(operation_stack and operation_stack[-1]) != "(":
                    output.append(operation_stack)
                operation_stack.pop()
            else:
                while(operation_stack and operation_stack[-1] != "(" and precendence[token] <= precendence[operation_stack[-1]]):
                    output.append(operation_stack.pop())
                    operation_stack.append(token)
    