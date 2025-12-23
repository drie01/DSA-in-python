 #push pop and peek with brackets
class Stack:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, value):
        self.elements.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        return None

def check_balanced_parentheses(expression):
    brackets = Stack()
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':  # Opening bracket # open huda chai push garcha ani close garda chai pop if its not empty
            brackets.push(char)
        elif char in ')}]':  # Closing bracket
            if brackets.is_empty() or brackets.pop() != matching[char]:
                return False
    
    return brackets.is_empty()

if __name__ == "__main__":
    test_expression = "{[()(){}]}"
    print("Expression:", test_expression, "-> Balanced:", check_balanced_parentheses(test_expression)) # prints balanced :truee when it is balanced .