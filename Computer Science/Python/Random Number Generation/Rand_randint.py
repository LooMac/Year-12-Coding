import random

##########################Subroutines##########################

def check(string,checkNum):
    for i in string:
        if i == checkNum:
            return True
        else:
            return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~Main Program~~~~~~~~~~~~~~~~~~~~~~~~~~

temp = 0
numList = [random.randint(1,49)]

for i in range(5):
    temp = random.randint(1,49)

    if check(numList,temp) == True:
        pass
    else:
        numList.append(temp)

print(numList)
