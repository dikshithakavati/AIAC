class Student:
    def __init__(self, name, rollno, cgpa):
        self.name = name
        self.rollno = rollno
        self.cgpa = cgpa
    
    def __repr__(self):
        return f"Name: {self.name}, Roll No: {self.rollno}, CGPA: {self.cgpa}"


def sort_students_by_cgpa(student_list):
    """
    Sort students by CGPA in descending order and display their details.
    
    Args:
        student_list (list): List of Student objects
        
    Returns:
        list: Sorted list of students by CGPA (descending)
    """
    # Sort students by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    
    # Display the sorted students
    print("\nStudents sorted by CGPA (Descending Order):")
    print("-" * 50)
    for i, student in enumerate(sorted_students, 1):
        print(f"{i}. {student}")
    
    return sorted_students


def display_top_10_students(student_list):
    """
    Display the top 10 students according to CGPA.
    
    Args:
        student_list (list): List of Student objects
        
    Returns:
        list: Top 10 students sorted by CGPA (descending)
    """
    # Sort students by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    
    # Get top 10 students
    top_10 = sorted_students[:10]
    
    # Display the top 10 students
    print("\n🏆 TOP 10 STUDENTS BY CGPA 🏆")
    print("=" * 60)
    for i, student in enumerate(top_10, 1):
        if i <= 3:  # Top 3 get special formatting
            print(f"🥇 Rank {i}: {student}")
        elif i <= 10:
            print(f"   Rank {i}: {student}")
    
    # Display summary statistics
    if top_10:
        print(f"\n📊 Top 10 Summary:")
        print(f"   Highest CGPA: {top_10[0].cgpa}")
        print(f"   10th Highest CGPA: {top_10[-1].cgpa}")
        avg_top_10 = sum(student.cgpa for student in top_10) / len(top_10)
        print(f"   Average CGPA of Top 10: {avg_top_10:.2f}")
    
    return top_10


def main():
    """
    Main function to demonstrate the sorting functionality.
    """
    # Sample student data
    students = [
        Student("Alice Johnson", "CS001", 3.8),
        Student("Bob Smith", "CS002", 3.2),
        Student("Carol Davis", "CS003", 3.9),
        Student("David Wilson", "CS004", 3.5),
        Student("Eva Brown", "CS005", 3.7),
        Student("Frank Miller", "CS006", 3.1),
        Student("Grace Taylor", "CS007", 3.6),
        Student("Henry Anderson", "CS008", 3.4),
        Student("Ivy Chen", "CS009", 3.95),
        Student("Jack Thompson", "CS010", 2.8),
        Student("Kelly Rodriguez", "CS011", 3.3),
        Student("Leo Martinez", "CS012", 3.75),
        Student("Maya Patel", "CS013", 3.85),
        Student("Noah Kim", "CS014", 2.9),
        Student("Olivia Garcia", "CS015", 3.65),
        Student("Peter Singh", "CS016", 3.25),
        Student("Quinn O'Brien", "CS017", 3.55),
        Student("Rachel White", "CS018", 3.15),
        Student("Sam Lee", "CS019", 3.45),
        Student("Tina Kumar", "CS020", 3.35),
        Student("Uma Sharma", "CS021", 2.75),
        Student("Victor Nguyen", "CS022", 3.6),
        Student("Wendy Zhang", "CS023", 3.4),
        Student("Xavier Lopez", "CS024", 3.05),
        Student("Yara Ahmed", "CS025", 3.5),
        Student("Zoe Foster", "CS026", 3.8),
        Student("Alex Turner", "CS027", 2.95),
        Student("Beth Cooper", "CS028", 3.7),
        Student("Chris Murphy", "CS029", 3.2),
        Student("Diana Ross", "CS030", 3.9)
    ]
    
    print("Original Student List:")
    print("-" * 50)
    for student in students:
        print(student)
    
    # Display top 10 students by CGPA
    top_10_students = display_top_10_students(students)
    
    # Sort and display all students by CGPA (optional - can be commented out for cleaner output)
    print("\n" + "="*60)
    sorted_students = sort_students_by_cgpa(students)
    
    return sorted_students


if __name__ == "__main__":
    main()
