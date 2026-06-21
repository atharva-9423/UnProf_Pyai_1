
class Person:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name, roll_no)
        self.grades = {}

    def add_grade(self, subject, marks):
        if subject in self.grades:
            print(f"⚠️  {subject} already exists. Use 'Update Grade' instead.")
        else:
            self.grades[subject] = marks
            print(f"✅ Added {subject}: {marks}")

    def update_grade(self, subject, marks):
        if subject in self.grades:
            old = self.grades[subject]
            self.grades[subject] = marks
            print(f"🔄 Updated {subject}: {old} -> {marks}")
        else:
            print(f"⚠️  {subject} not found. Use 'Add Grade' instead.")

    def display_report_card(self):
        print("\n" + "=" * 40)
        print("STUDENT REPORT CARD".center(40))
        print("=" * 40)
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print("-" * 40)

        if not self.grades:
            print("No grades recorded yet.")
            print("=" * 40)
            return

        total = 0
        print(f"{'Subject':<20}{'Marks':<10}")
        for subject, marks in self.grades.items():
            print(f"{subject:<20}{marks:<10}")
            total += marks

        average = total / len(self.grades)
        result = "PASS" if average >= 40 else "FAIL"

        print("-" * 40)
        print(f"Total Marks : {total}")
        print(f"Average     : {average:.2f}")
        print(f"Result      : {result}")
        print("=" * 40)

def main():
    print("----- Register Student -----")
    name = input("Enter Student Name: ").strip()
    roll_no = input("Enter Roll Number: ").strip()
    student = Student(name, roll_no)

    while True:
        print("\n===== STUDENT MANAGEMENT MENU =====")
        print("1. Add Grade")
        print("2. Update Grade")
        print("3. Display Report Card")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            subject = input("Enter Subject Name: ").strip()
            marks = get_valid_marks()
            student.add_grade(subject, marks)

        elif choice == "2":
            subject = input("Enter Subject Name: ").strip()
            marks = get_valid_marks()
            student.update_grade(subject, marks)

        elif choice == "3":
            student.display_report_card()

        elif choice == "4":
            print("✅ Exiting Program...")
            break

        else:
            print("❌ Invalid choice! Please enter 1-4.")

def get_valid_marks():
    while True:
        raw = input("Enter Marks (0-100): ").strip()
        try:
            marks = int(raw)
            if 0 <= marks <= 100:
                return marks
            print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a whole number.")

if __name__ == "__main__":
    main()
