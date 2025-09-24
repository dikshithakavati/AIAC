class Student:
    """Represents a student with name, age, and a list of marks."""

    def __init__(self, name, age, marks):
        """Initialize student with descriptive attributes.

        Args:
            name: Student's name (string).
            age: Student's age (int or convertible to int).
            marks: Iterable of numeric marks (list of int/float).
        """
        self.name = name
        self.age = int(age)
        self.marks = list(marks)

    def details(self):
        """Print student details in a readable format."""
        print(f"Name: {self.name} | Age: {self.age}")

    def total(self):
        """Return the total of all marks."""
        return sum(self.marks)


def read_student_from_console():
    """Prompt user for student details and return a Student object."""
    name = input("Enter name: ").strip()
    age_str = input("Enter age: ").strip()
    marks_str = input("Enter marks separated by spaces: ").strip()

    age = int(age_str)
    marks = [float(x) for x in marks_str.split()] if marks_str else []
    return Student(name, age, marks)


if __name__ == "__main__":
    try:
        student = read_student_from_console()
        student.details()
        print(f"Total Marks: {student.total()}")
    except ValueError as e:
        print(f"Invalid input: {e}")