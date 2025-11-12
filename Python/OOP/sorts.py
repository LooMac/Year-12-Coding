import time
import random

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        # Start timer
        start_time = time.time()
        
        n = len(self.arr)
        
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already sorted, no need to check them
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

        # End timer
        end_time = time.time()

        # Calculate the time taken
        self.time_taken = end_time - start_time

    def get_sorted_array(self):
        return self.arr

    def get_time_taken(self):
        return self.time_taken


