def generate_email_ids(names):
    emails = []
    for name in names:
        parts = name.strip().split()
        if len(parts) < 2:
            continue  # Skip if not enough parts
        first_letter = parts[0][0].lower()
        last_name = parts[-1].lower()
        email = f"{first_letter}{last_name}@sru.edu.in"
        emails.append(email)
    return emails

# Take user input
num_students = int(input("Enter number of students: "))
student_names = []
for _ in range(num_students):
    name = input("Enter student name: ")
    student_names.append(name)

for email in generate_email_ids(student_names):
    print(email)