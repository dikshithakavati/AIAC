"""Unit tests for `Student` and the demo in `task1.py`.

Test descriptions (plain-English):
- Test 1: Verify that marking attendance updates the stored records and
  that the counts/properties reflect the changes.
- Test 2: Verify that percentage calculation is correct for a mixed
  present/absent sequence (example: 2 present out of 3 -> 66.666...).
- Test 3: Verify the demo example returns expected values for the
  5-day sample (3 present out of 5 -> 60.0%).
"""

import unittest

from task1 import Student, demo_attendance


class TestStudent(unittest.TestCase):
    def test_marking_and_properties(self):
        """Test 1: Attendance marking updates records and properties."""
        s = Student(name="Bob", student_id="S002")
        s.mark_attendance(True)
        s.mark_attendance(False)
        self.assertEqual(s.total_classes, 2)
        self.assertEqual(s.attended_classes, 1)

    def test_percentage_mixed(self):
        """Test 2: Percentage is correct for a mixed sequence."""
        s = Student(name="Dana", student_id="S004")
        s.mark_attendance(True)
        s.mark_attendance(False)
        s.mark_attendance(True)
        expected = (2 / 3) * 100.0
        self.assertAlmostEqual(s.attendance_percentage(), expected, places=7)

    def test_demo_example(self):
      """Test 3: Demo example produces the expected totals, absent and percentage."""
      total, present, pct, absent = demo_attendance()
      self.assertEqual(total, 5)
      self.assertEqual(present, 3)
      self.assertEqual(absent, 2)
      self.assertAlmostEqual(pct, 60.0)


if __name__ == "__main__":
    unittest.main()
