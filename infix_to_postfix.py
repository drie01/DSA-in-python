# Stack class
class Stack:
    def __init__(self):
        # this list will act like our stack
        self.elements = []

    def is_empty(self):
        # stack is empty when list has no items
        return len(self.elements) == 0

    def push(self, value):
        # push basically means adding to the end
        self.elements.append(value)

    def pop(self):
        # pop from end, but only if non-empty
        if not self.is_empty():
            return self.elements.pop()
        return None

    def peek(self):
        # peek means “show me the top element but don’t remove it”
        if not self.is_empty():
            return self.elements[-1]
        return None


def infix_to_postfix(expression):
    """
    Converts an infix expression to a postfix expression
    using the Shunting-Yard Algorithm.

    Assumes tokens are separated by spaces.
    Handles operators +, -, *, /, ^ and parentheses.

    Args:
        expression (str): The infix expression (e.g., "( A + B ) * C")

    Returns:
        str: The equivalent postfix expression (e.g., "A B + C *")
    """

    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    output = []
    operator_stack = []

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            # Token is an operand (number or variable)
            output.append(token)

        elif token == '(':
            # Token is a left parenthesis
            operator_stack.append(token)

        elif token == ')':
            # Token is a right parenthesis
            # Pop operators until matching '(' is found
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Discard '('

        else:
            # Token is an operator
            while (
                operator_stack
                and operator_stack[-1] != '('
                and precedence.get(operator_stack[-1], 0)
                >= precedence.get(token, 0)
            ):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    # Pop any remaining operators from the stack
    while operator_stack:
        output.append(operator_stack.pop())

    return " ".join(output)


# Example usage
infix_expr = "( A + B ) * C - ( D / E )"
postfix_expr = infix_to_postfix(infix_expr)

print(f"Infix: {infix_expr}")
print(f"Postfix: {postfix_expr}")
