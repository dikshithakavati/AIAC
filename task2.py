def cm_to_inches(cm):
    """
    Convert centimeters to inches.
    
    Conversion factor: 1 cm = 0.39 inches
    
    Args:
        cm (float): Length in centimeters
        
    Returns:
        float: Length in inches
    """
    return cm * 0.39


# Get input from console and convert cm to inches
if __name__ == "__main__":
    try:
        cm = float(input("Enter length in centimeters: "))
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches:.2f} inches")
    except ValueError:
        print("Please enter a valid number.")
