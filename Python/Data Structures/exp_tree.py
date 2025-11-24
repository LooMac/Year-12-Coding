class Node():
    def __init__(self, given_value):
        self.left = None
        self.right = None
        self.value = given_value

class ExpressionTree():
    def __init__(self):
        self.root = None

    def build_tree(self, postfix_expression):
        stack = []

        for char in postfix_expression:
            if char.isalnum():  # If the character is an operand
                node = Node(char)
                stack.append(node)
            else:  # The character is an operator
                right_node = stack.pop()
                left_node = stack.pop()
                operator_node = Node(char)
                operator_node.left = left_node
                operator_node.right = right_node
                stack.append(operator_node)

        self.root = stack.pop()
    
    def inorder_traversal(self, node):
        if node is not None:
            return (self.inorder_traversal(node.left) +
                    str(node.value) +
                    self.inorder_traversal(node.right))
        return ""
# Example usage:
exp_tree = ExpressionTree()
exp_tree.build_tree("ab+cde+**")
print("Inorder Traversal of the Expression Tree:")
print(exp_tree.inorder_traversal(exp_tree.root))  # Output: a+b*c