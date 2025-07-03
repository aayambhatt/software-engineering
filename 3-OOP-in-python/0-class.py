class Student:
    def __init__(self, roll_no, name, age, subjects):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.subjects = subjects

    def display_info(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Subjects:", ", ".join(self.subjects))

student1 = Student(roll_no="211B006", name="Aayam Bhatt", age=22,subjects=["Software Engineering", "Data Structures and Algorithms"])
student1.display_info()
        
