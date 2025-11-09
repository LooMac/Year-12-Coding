notValueErr = False
while notValueErr == False:
    try:
            num1 = int(input("Enter a number between 0 and 10: "))
    except ValueError:
            print("You have not entered a numerical value.")
            num1 = int(input("\nEnter a number between 0 and 10: "))
            
    finally:
        notValueErr = True
        while num1 < 0 or num1 > 10:
            print("\nYou have entered a numerical value, however it is not valid.")
            num1 = int(input("Enter a number between 0 and 10: "))
        else:
            print("\nYou have entered a numerical value, and it is valid.")
