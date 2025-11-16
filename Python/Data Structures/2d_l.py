import sys

class Student():
    def __init__(self):
        self.name, self.score = self.__get_student_info()
    def __repr__(self):
        return f"name : {self.name}, score : {self.score}"
    def __get_student_info(self):
        try:
            name = str(input("Enter student name: "))
            score = int(input("Enter student score: "))
            if name == "" or score < 0:
                raise ValueError
            return name, score
        except:
            print("Invalid input. Please enter a valid name and score.")
            return self.__get_student_info()
        
def create_student_list():
    student_list = []
    yorn = 'y'
    while yorn.lower() == 'y':
        student = Student()
        student_list.append(student)
        while True:
            yorn = input("Do you want to add another student? (y/n/exit): ")
            if yorn.lower() == 'exit':
                sys.exit()
            try:
                if yorn.lower() not in ['y', 'n']:
                    raise ValueError
                break
            except:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue
    return student_list

if __name__ == "__main__":
    students = create_student_list()
    for student in students:
        print("\n"+str(student))