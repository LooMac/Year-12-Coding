from queue import Queue

class Customer():
    def __init__(self, given_name: str):
        self.name = given_name

class PostOffice():
    def __init__(self):
        self.post_office_queue = Queue(maxsize = 6)
    
    def display_queue(self):
        #Procedure to output full queue
        if not self.post_office_queue.empty():
            size = self.post_office_queue.qsize()
            print(f"\nPost Office Queue of size {size}:")
            for i in range(size):
                customer = self.post_office_queue.get()     #Dequeue customer
                print(customer.name)               #Display customer name
                self.post_office_queue.put(customer)        #Reinsert customer back into the queue

    def remove_customer(self):
        #Procedure to deqeue the first customer
        if not self.post_office_queue.empty():
            removed_customer = self.post_office_queue.get()
            print(f"\n{removed_customer.name} has been served and removed from the queue")

    def add_customer(self, given_customer: object):
        #Procedure to enqeue new customer into the post
        #office queue
        if not self.post_office_queue.full():
            self.post_office_queue.put(given_customer)
            print(f"\n{given_customer.name} has entered the queue")

def main():
    post_office_1 = PostOffice()
    customer_1 = Customer("Phil")
    post_office_1.add_customer(customer_1)
    customer_2 = Customer("Alice")
    post_office_1.add_customer(customer_2)
    customer_3 = Customer("Olivia")
    post_office_1.add_customer(customer_3)
    customer_4 = Customer("John")
    post_office_1.add_customer(customer_4)
    customer_5 = Customer("Phoebe")
    post_office_1.add_customer(customer_5)
    customer_6 = Customer("Robert")
    post_office_1.add_customer(customer_6)
    post_office_1.display_queue()

if __name__ == "__main__":
    main()