# making a node class so we can build our own linked-list-based stack
from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional['Node'] = None
        
class Stack:
    def __init__(self):
        self.top = None  # this will point to the topmost element in the stack

    def is_empty(self):
        # if top is none, stack is empty
        return self.top is None

    def push(self, value,):
        # create a new node and make it the new top
        new_node = Node(value)
        new_node.next = self.top  # link it to the old top
        self.top = new_node       # update top pointer

    def pop(self):
        # if nothing to pop, just return none
        if self.is_empty():
            return None

        # take the top element
        if self.top is not None:
            popped_value = self.top.value
            self.top = self.top.next  # move top pointer down
            return popped_value
        return None


# function to check if parentheses/brackets are balanced
def check_balanced_parentheses(expression):
    stack = Stack()
    
    # dictionary for matching closing -> opening bracket
    matching = {')': '(', '}': '{', ']': '['}

    # loop through every character in the input string
    for char in expression:
        # if it's an opening bracket, throw it on the stack
        if char in '({[':
            stack.push(char)

        # if it's a closing bracket
        elif char in ')}]':
            # stack empty means there's nothing to match with
            if stack.is_empty():
                return False

           # pop something and compare
            if stack.pop() != matching[char]: # if not matching, return false else continue
                return False

    # at the end if stack is empty
    return stack.is_empty()


#test
if __name__ == "__main__": #optional
    test_expression = "{[()()]}"
    print("expression:", test_expression, "-> balanced:", check_balanced_parentheses(test_expression))
