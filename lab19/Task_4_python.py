def print_students(students):
    """
    Print a list of student names with numbering.
    Args:
        students: A list of student names
    """
    # Check if the input is a list
    if not isinstance(students, list):
        print("Error: Input must be a list of student names")
        return

    # Print each student name with numbering
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")

# Test cases
student_list = ["John", "Alice", "Bob", "Emma"]
print("List of Students:")
print_students(student_list)

# Test with empty list
print("\nEmpty List:")
print_students([])

# Test with invalid input
print("\nInvalid Input Test:")
print_students("Not a list")