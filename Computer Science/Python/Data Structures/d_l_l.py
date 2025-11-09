class Node():
    def __init__(self, given_data):
        self.data = given_data
        self.next = None
        self.prev = None

class DLL():
    def __init__(self, given_values):
        self.__values = given_values
        self.__head = self.__create_doubly_linked_list()
    
    def print_list(self):
        temp = self.__head
        
        while temp:
            print(temp.data, end = "")
            
            if temp.next:
                print(" <-> ", end = "")
            
            temp = temp.next
            
    def __create_doubly_linked_list(self):
        head = None
        prev = None

        for val in self.__values:
            new_node = Node(val)
            if head is None:
                head = new_node  # First node becomes the head
            else:
                prev.next = new_node  # Link previous node to current
                new_node.prev = prev  # Link current node back to previous
            prev = new_node  # Move prev to current node for next iteration

        return head


# 1 <-> 2 <-> 3 <-> 4 ...

d_l_l_1 = DLL([1,2,3,4,5,6])

d_l_l_1.print_list()
