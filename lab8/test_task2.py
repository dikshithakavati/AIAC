import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_valid_grades(self):
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(79.9), "C")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(69.9), "D")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(59.9), "F")
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(50), "F")

    def test_invalid_types(self):
        self.assertEqual(assign_grade("80"), "Invalid")
        self.assertEqual(assign_grade(None), "Invalid")
        self.assertEqual(assign_grade([80]), "Invalid")
        self.assertEqual(assign_grade({}), "Invalid")

    def test_out_of_range(self):
        self.assertEqual(assign_grade(-1), "Invalid")
        self.assertEqual(assign_grade(-100), "Invalid")
        self.assertEqual(assign_grade(101), "Invalid")
        self.assertEqual(assign_grade(150), "Invalid")

if __name__ == "__main__":
    unittest.main()