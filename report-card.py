class Person:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name, roll_no)
        self.grades = {}

    def add_grade(self, subject, marks):
        self.grades[subject] = marks
        print(f"{subject} grade added/updated successfully.")

    def display_report(self):
        print("\n========== REPORT CARD ==========")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")

        if not self.grades:
            print("No grades available.")
            return

        total = 0

        print("\nSubjects and Grades:")
        for subject, marks in self.grades.items():
            print(f"{subject}: {marks}")
            total += marks

        average = total / len(self.grades)

        print("\nTotal Marks :", total)
        print("Average     :", round(average, 2))

        if average >= 40:
            print("Result      : PASS")
        else:
            print("Result      : FAIL")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

student = Student(name, roll_no)

num_subjects = int(input("How many subjects? "))

for i in range(num_subjects):
    subject = input("\nEnter Subject Name: ")
    marks = int(input("Enter Marks: "))
    student.add_grade(subject, marks)

student.display_report()