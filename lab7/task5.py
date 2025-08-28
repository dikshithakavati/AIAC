class StudentRecord:
    def __init__(self, name, id, courses=[]):
        self.studentName = names
        self.student_id = id
        self.courses = courseList

    def add_course(self, course):
        self.courses.append(course)

    def get_summary(self):
        return f"Student: {self.studentName}, ID: {self.student_id}, Courses: {', '.join(self.courses)}"

class Department:
    def __init__(self, deptName, students=None):
        self.dept_name = deptName
        self.students = students

    def enroll_student(self, student):
        self.students.append(student)

    def department_summary(self):
        return f"Department: {self.dept_name}, Total Students: {len(self.student)}"
        

s1 = StudentRecord("Alice", 101, ["Math", "Science"])
d1 = Department("Computer Science")
d1.enroll_student(s1)
print(s1.get_summary())
print(d1.department_summary())
def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(len(values)):
            # Avoid division by zero when i equals j
            if i != j:
                try:
                    ratio = values[i] / (values[j] - values[i])
                    results.append((i, j, ratio))
                except ZeroDivisionError:
                    # Skip if denominator is zero
                    continue
    return results