def format_name(full_name):
    """
    Convert a full name from "First Last" format to "Last, First" format.
    
    Args:
        full_name (str): Full name in "First Last" format
        
    Returns:
        str: Name in "Last, First" format
    """
    # Split the full name into first and last name
    name_parts = full_name.split()
    
    # Check if we have exactly two parts (first and last name)
    if len(name_parts) == 2:
        first_name = name_parts[0]
        last_name = name_parts[1]
        return f"{last_name}, {first_name}"
    else:
        return "Invalid name format. Please enter 'First Last'"


# Get input from console and format the name
if __name__ == "__main__":
    full_name = input("Enter full name (First Last): ")
    result = format_name(full_name)
    print(result)
