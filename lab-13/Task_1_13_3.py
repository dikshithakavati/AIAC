def area_rectangle(length, width):
    """Calculate area of a rectangle."""
    return length * width

def area_square(side):
    """Calculate area of a square."""
    return side * side

def area_circle(radius):
    """Calculate area of a circle."""
    return 3.14 * radius * radius

def calculate_area(shape, x, y=0):
    """Calculate area based on shape type."""
    shape = shape.lower()
    if shape == "rectangle":
        return area_rectangle(x, y)
    elif shape == "square":
        return area_square(x)
    elif shape == "circle":
        return area_circle(x)
    else:
        raise ValueError(f"Unknown shape: {shape}")

if __name__ == "__main__":
    try:
        shape = input("Enter shape (rectangle/square/circle): ").strip()
        if shape.lower() == "rectangle":
            length = float(input("Enter length: ").strip())
            width = float(input("Enter width: ").strip())
            area = calculate_area(shape, length, width)
        elif shape.lower() == "square":
            side = float(input("Enter side: ").strip())
            area = calculate_area(shape, side)
        elif shape.lower() == "circle":
            radius = float(input("Enter radius: ").strip())
            area = calculate_area(shape, radius)
        else:
            raise ValueError("Invalid shape. Choose rectangle, square, or circle.")

        print(f"Area: {area}")
    except ValueError as e:
        print(f"Error: {e}")