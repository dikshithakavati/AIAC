"""
task1.py

Student class for a smart attendance app.

This module implements a `Student` class that stores attendance records,
provides methods to mark attendance and calculate the attendance percentage,
and includes a small demo helper that shows the example output described by
the user.

The class stores per-day attendance in `attendance_records` (list of bool),
so the full history is available for further features (reporting, persistence,
etc.).
"""

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Student:
    """Represents a student and their attendance record.

    Attributes:
        name: Student's full name.
        student_id: Unique identifier for the student.
        attendance_records: List of booleans where True means present and
            False means absent for each class session in chronological order.

    Methods:
        mark_attendance(present): Record attendance for one class.
        attendance_percentage(): Return percent of classes attended.
    """

    name: str
    student_id: str
    attendance_records: List[bool] = field(default_factory=list, init=False)

    def mark_attendance(self, present: bool) -> None:
        """Mark attendance for a single class session.

        Args:
            present: True if the student was present, False if absent.

        This method appends the attendance status to `attendance_records`.
        Keeping the raw per-day records allows later reporting and avoids
        inconsistencies from separately maintained counters.
        """
        # Append the day's attendance (True for present, False for absent).
        self.attendance_records.append(bool(present))

    @property
    def total_classes(self) -> int:
        """Return the total number of classes for which attendance was recorded."""
        return len(self.attendance_records)

    @property
    def attended_classes(self) -> int:
        """Return the number of classes the student was present for."""
        return sum(1 for present in self.attendance_records if present)

    def attendance_percentage(self) -> float:
        """Calculate and return the attendance percentage.

        Returns:
            A float between 0.0 and 100.0. If no classes have been recorded,
            the function returns 0.0 to avoid division by zero.
        """
        total = self.total_classes
        if total == 0:
            return 0.0
        return (self.attended_classes / total) * 100.0

    def __repr__(self) -> str:  # pragma: no cover - trivial representation
        return (
            f"Student(name={self.name!r}, student_id={self.student_id!r}, "
            f"attended={self.attended_classes}, total={self.total_classes})"
        )


def demo_attendance(name: str = "Dikshitha", student_id: str = "S100") -> Tuple[int, int, float, int]:
    """Run the example attendance scenario and print the expected output.

    The example uses the 5-day sequence from the user's description:
        [Present, Absent, Present, Present, Absent]

    Returns:
        A tuple (total_days, present_days, percentage) to allow automated tests
        to verify the results without parsing stdout.
    """
    s = Student(name=name, student_id=student_id)
    example_records = [True, False, True, True, False]
    for r in example_records:
        s.mark_attendance(r)

    total = s.total_classes
    present = s.attended_classes
    pct = s.attendance_percentage()

    # Print the friendly, example output requested by the user.
    print("Attendance marked successfully.")
    print(f"Total days: {total}")
    print(f"Present days: {present}")
    print(f"Attendance Percentage: {pct}%")

    absent = total - present

    # Print the friendly, example output requested by the user.
    print("Attendance marked successfully.")
    print(f"Total days: {total}")
    print(f"Present days: {present}")
    print(f"Absent days: {absent}")
    print(f"Attendance Percentage: {pct}%")

    return total, present, pct, absent


def interactive_attendance() -> Tuple[int, int, float, int]:
    """Interactive CLI to collect attendance from the user.

    Prompts the user for a student name and id, then asks how many days to
    record and for each day asks whether the student was present. Input is
    validated: number of days must be a non-negative integer and each day's
    response must be 'y'/'n' (or variants).

    Returns:
        A tuple (total_days, present_days, percentage) so callers (and tests)
        can programmatically inspect results.
    """
    print("Interactive attendance input")
    name = input("Enter student name (leave blank for 'Dikshitha'): ").strip()
    if not name:
        name = "Dikshitha"

    student_id = input("Enter student id (leave blank for 'S100'): ").strip()
    if not student_id:
        student_id = "S100"

    # get number of days
    while True:
        days_str = input("Enter number of days to record (0 for none): ").strip()
        try:
            days = int(days_str)
            if days < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of days.")

    s = Student(name=name, student_id=student_id)
    for i in range(1, days + 1):
        while True:
            resp = input(f"Day {i} - Present? (y/n): ").strip().lower()q
            if resp in {"y", "yes"}:
                s.mark_attendance(True)
                break
            if resp in {"n", "no"}:
                s.mark_attendance(False)
                break
            print("Please answer 'y' or 'n'.")

    total = s.total_classes
    present = s.attended_classes
    pct = s.attendance_percentage()

    absent = total - present

    print("Attendance marked successfully.")
    print(f"Total days: {total}")
    print(f"Present days: {present}")
    print(f"Absent days: {absent}")
    print(f"Attendance Percentage: {pct}%")

    return total, present, pct, absent


if __name__ == "__main__":
    # When executed directly, run the interactive prompt so the user can
    # input student details and attendance day-by-day.
    interactive_attendance()
