class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Marks: {self.marks}")
    
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
a = student("John", 20, 95)
a.display()
print(f"Grade: {a.calculate_grade()}")
