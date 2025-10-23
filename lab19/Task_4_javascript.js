function printStudents(students) {
    // Check if the input is an array
    if (!Array.isArray(students)) {
        console.log("Error: Input must be an array of student names");
        return;
    }

    // Print each student name
    students.forEach((student, index) => {
        console.log(`${index + 1}. ${student}`);
    });
}

// Test cases
const studentList = ["John", "Alice", "Bob", "Emma"];
console.log("List of Students:");
printStudents(studentList);

// Test with empty array
console.log("\nEmpty List:");
printStudents([]);

// Test with invalid input
console.log("\nInvalid Input Test:");
printStudents("Not an array");