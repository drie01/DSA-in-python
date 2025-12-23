#AVL tree
from typing import List,Optional,Any
from collections import deque
class AVLNode:
    def __init__(self,key:int):
        self.key = key
        self.left : Optional['AVLNode'] = None
        self.right : Optional['AVLNode'] = None
        self.height = 1

class AVLTree:
    def get_height(self,node: Optional[AVLNode])-> int:
        return node.height if node else 0 
    
    def get_balance(self,node:Optional[AVLNode])-> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0 
    
    def _update_height(self,node:AVLNode)-> None:
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
    
    def right_rotate(self,y:AVLNode) -> AVLNode:
        #perform rotation
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        #update heights
        self._update_height(y)
        self._update_height(x)

    def left_rotate(self,x:AVLNode) -> AVLNode:
        #perform rotation
       y = x.right
       T2 = y.left

       y.left = x
       x.right = T2

        #update heights
        self._update_height(x)
        self._update_height(y)

    

    def insert(self,root:Optional[AVLNode],key:int) -> AVLNode:
        #1.standard BST insertion
        if not root:
            return AVLNode(key)

        elif key < root.key:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)
        
        #2. update heiht on this ancestor node
        self._update_height(root)

        #3. get the balance factor
        balance = self.get_balance(root)
        
        #4 rebalance if needed
        #left left case
        if balance > 1  and key < root.left.key:
            return self.right_rotate(root)
        
        #right right case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        #left right case
        if balance > 1 and key> root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance <- 1 and key <root.right.key:
            root.right = self.right_rotate(root.right)
            return self.right_rotate(root)
        return root
 
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    #inserting in sorted order
    #in a normal BST, this would result in a height of 6(skewed)
    # in an AVl tree ,it should balance itself
    keys = [10,20,30,40,50,25]
    print(f"Insering keys : {keys}")

    for key in keys:
        root = avl.insert(root,key)
