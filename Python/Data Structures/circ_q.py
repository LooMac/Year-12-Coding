class MyCircularQueue():
    def __init__(self, given_max_size):
        self.__max_size = given_max_size
        self.__array = [0] * given_max_size
        self.__front = 0
        self.__size = 0

    def enqueue(self, given_element):
        #Check if queue is full
        if self.__size == self.__max_size:
            print("Queue already full")
            return
        #If not full enqueue element at rear
        rear = (self.__front + self.__size) % self.__max_size
        self.__array[rear] = given_element
        self.__size += 1
    
    def dequeue(self):
        #Check if queue is empty
        if self.__size == 0:
            print("Queue is already empty")
            return -1
        #If not empty dequeue, dequeue element at front and return it
        result = self.__array[self.__front]
        self.__front = (self.__front + 1) % self.__max_size
        self.__size -= 1
        return result
        

def main():
    circular_queue_1 = MyCircularQueue(5)
    circular_queue_1.enqueue(10)

if __name__ == "__main__":
    main()
