class Node():
    def __init__(self, given_data):
        self.data = given_data
        self.next = none
    
class Stack():
    def __init__(self):
        self.__head = none
        self.__size = 0

    def is_empty(self):
        #If length of node list > 0 return False
        return self.__size == 0

    def push(self, given_data):
        new_node = Node(given_data)
        if not self.is_empty:
            new_node.next = self.__head 
        self.__head = new_node
        self.__size += 1

        
