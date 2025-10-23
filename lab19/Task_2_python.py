def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test cases
print(check_number(5))    # Should print "Positive"
print(check_number(-3))   # Should print "Negative"
print(check_number(0))    # Should print "Zero"