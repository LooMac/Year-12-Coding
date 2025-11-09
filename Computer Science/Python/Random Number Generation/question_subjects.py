from datetime import date
import random

####################### SUBROUTINES #######################

def printDate():
    dateToday = date.today()
    print(f"Date of test: {dateToday}\n")

def questions(subjects):
    for i in subjects:
        temp = random.randint(1,10)
        print(f"{i}: Select the question number: {temp}")

def main():
    subjects = ["Programming","Databases","Networking","Data Structures","Algorithms"]
    printDate()
    print("-------- List of topics with question numbers --------\n")
    questions(subjects)
    
#~~~~~~~~~~~~~~~~~~~~~~ MAIN PROGRAM ~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    main()
