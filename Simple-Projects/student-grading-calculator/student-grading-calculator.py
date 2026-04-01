class Student:
    def __init__(self, fullname, marks, max_marks):
        self.name = fullname
        self.marks = marks
        self.max_marks = max_marks   
        self.grade()

    def grade(self):
        percentage = (self.marks / self.max_marks) * 100
        
        if percentage > 90:
            print(f"{self.name}: Grade A ({percentage:.2f}%)\n")
        elif percentage > 80:
            print(f"{self.name}: Grade B ({percentage:.2f}%)\n")
        elif percentage > 70:
            print(f"{self.name}: Grade C ({percentage:.2f}%)\n")
        elif percentage > 40:
            print(f"{self.name}: Grade D ({percentage:.2f}%)\n")
        else:
            print(f"{self.name}: Fail! ({percentage:.2f}%)\n")


# Main loop
while True:
    try:
        name1 = input("Enter Name of the Student (or 'quit' to exit): ").strip()
        if name1.lower() == 'quit':
            print("Exiting program. Bye!\n")
            break

        marks_input = input("Enter Marks/Max marks (e.g. 85/100): ").strip()
        marks1 = marks_input.split("/")
        
        if len(marks1) != 2:
            raise ValueError("Please enter in format: Marks/Max marks (like 85/100)")

        marks = int(marks1[0].strip())
        max_marks = int(marks1[1].strip())

        if marks > max_marks:
            raise ValueError("Marks cannot be higher than Max marks")
        if marks < 0 or max_marks < 0:
            raise ValueError("No negative values please")
        if max_marks == 0:
            raise ValueError("Maximum marks cannot be zero")
        s1 = Student(name1, marks, max_marks)

    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.\n")
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Please try again.\n")
