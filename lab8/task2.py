def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid"
    
    if score < 0 or score > 100:
        return "Invalid"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    print(assign_grade(95))    # A
    print(assign_grade(75))    # C
    print(assign_grade(-5))    # Invalid
    print(assign_grade("80"))  # Invalid