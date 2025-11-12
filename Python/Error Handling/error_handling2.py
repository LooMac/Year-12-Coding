
###############SUBROUTINES###############
def enterNums():
    try:
        nums=[]
        for i in range(2): nums.append(int(input("Enter two numbers: ")))
        return nums
    except ValueError:
        print("An entry is invalid.")
        nums = []
        for i in range(2): nums.append(int(input("Enter two numbers: ")))
    
def division(nums):
    try:
        num3 = nums[0] / nums[1]
        print(f"The quotient of {nums[0]} and {nums[1]} is {num3}")
    except ZeroDivisionError:
        print("You can not divide by 0.")

###############MAIN PROGRAM###############

numList = enterNums()
division(numList)
