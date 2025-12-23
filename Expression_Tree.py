from typing import List, Optional, Any
from collections import deque

class ExpressionNode:
    def __init__(self,value:str):
        self.value = value
        self.left: Optional['ExpressionNode'] = None
        self.right: Optional['ExpressionNode'] = None


class ExpressionTree:
    @staticmethod
    def evaluate(node: Optional[ExpressionNode]) -> float:
        # evaluates the expression tree: +-*/
        if not node:
            return  0.0
        
        # base case: leaf node(operand)
        if node.left is None and node.right is None:
                    if node.value in ["+","-","*","/"]:
                        raise ValueError("No operand found")
                        return 0.0
                    
                    return float(node.value)
        
        # recursive step: evaluate childern
        left_val = ExpressionTree.evaluate(node.left)
        right_val = ExpressionTree.evaluate(node.right)

        # Apply operator
        if node.value == '+': return left_val + right_val
        if node.value == '-': return left_val - right_val
        if node.value == '*': return left_val * right_val
        if node.value == '/':
            if right_val == 0: raise ValueError("Division by zero")
            return left_val / right_val
        
        raise ValueError(f"Unknown Operator: {node.value}")
    

if __name__ == "__main__":
    # Representing equation: (3 + 4) * 2
    #         *
    #       /   \
    #      +      2
    #     / \
    #    3   4    


    expr_root = ExpressionNode('*')
    expr_root.right = ExpressionNode('2')
    expr_root.left = ExpressionNode('+')
    expr_root.left.left = ExpressionNode('3')
    expr_root.left.right = ExpressionNode('4')

    result = ExpressionTree.evaluate(expr_root)
    print(f"Evaluationg (3 + 4) * 2: {result}")