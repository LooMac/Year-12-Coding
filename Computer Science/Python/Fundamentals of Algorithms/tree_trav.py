class Node:
    def __init__(self, given_key):
        self.val = given_key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
            return root
    if root.val < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root

def preorder(root):
    print(root.val, end = " ")
    
    if root.left:
        preorder(root.left)
    
    if root.right:
        preorder(root.right)
        
r = Node(5)
r = insert(r, 3)
r = insert(r, 6)
r = insert(r, 2)
r = insert(r, 4)
r = insert(r, 8)
r = insert(r, 1)
r = insert(r, 7)

preorder(r)
