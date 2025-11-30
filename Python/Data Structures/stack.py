class Node():
    def __init__(self, given_data):
        self.data = given_data
        self.next = None
    
class Stack():
    def __init__(self):
        self.__head = None
    
    def push(self, given_data):
        new_node = Node(given_data)
        new_node.next = self.__head
        self.__head = new_node

    def pop(self):
        if self.__head is None:
            print("Stack Underflow")
            return -1
        
        node_to_pop = self.__head
        self.__head = self.__head.next
        data = node_to_pop.data

        del node_to_pop
        return data

stack_1 = Stack()
stack_1.push("H")
stack_1.push("e")
stack_1.push("l")
stack_1.push("l")
stack_1.push("o")

print(stack_1.pop(),end="")
print(stack_1.pop(),end="")
print(stack_1.pop(),end="")
print(stack_1.pop(),end="")
print(stack_1.pop(),end="")