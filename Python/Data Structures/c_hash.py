import hashlib

class HashTable:
    def __init__(self, given_size):
        self.size = given_size
        self.table = [[] for _ in range(given_size)]

    def hash(self, key):
        # Using MD5 hash function for better distribution
        # Convert the hash to an integer and take modulo with table size
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % self.size
    
    def insert(self, key, value):
        # Insert key-value pair into the hash table
        index = self.hash(key)
        # Check if the key already exists and update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If key does not exist, append new key-value pair
        self.table[index].append((key, value))
    
    def get(self, key):
        # Retrieve value by key from the hash table
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found
    
    def remove(self, key):
        # Remove key-value pair from the hash table
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False  # Key not found
    
    

