import random

nums = []
randNum = 0

def search(list, searchNum):
    for i in list:
        if list[i] == searchNum:
            return True

for i in range(5):
    randNum = random.randint(1,49)
    
