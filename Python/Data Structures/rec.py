# Student Information Management

class Student:
    def __init__(self, first_name, last_name, dob, email):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email

    def save_to_file(self):
        with open('students.txt', 'a') as file:
            file.write(f"{self.first_name}, {self.last_name}, {self.dob}, {self.email}\n")


def main():
    students = []

    for _ in range(3):
        while True:
            try:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                dob = input("Enter Date of Birth (YYYY-MM-DD): ")
                email = input("Enter email address: ")

                if not first_name or not last_name or not dob or not email:
                    raise ValueError("All fields are required.")
                
                if "@" not in email or "." not in email:
                    raise ValueError("Invalid email format.")
                
                if len(dob) != 10 or dob[4] != '-' or dob[7] != '-':
                    raise ValueError("Date of Birth must be in YYYY-MM-DD format.")

                student = Student(first_name, last_name, dob, email)
                student.save_to_file()
                students.append(student)
                break
            except Exception as e:
                print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    main()
