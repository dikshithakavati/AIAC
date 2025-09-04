def convert_date_format(date_str):
    parts = date_str.split("-")
    # Check for exactly 3 parts and correct lengths (YYYY-MM-DD)
    if len(parts) != 3:
        raise ValueError("Invalid format")
    year, month, day = parts
    if not (year.isdigit() and len(year) == 4 and month.isdigit() and len(month) == 2 and day.isdigit() and len(day) == 2):
        raise ValueError("Invalid format")
    return f"{day}-{month}-{year}"

if __name__ == "__main__":
    print(convert_date_format("2023-10-15"))  # Output: 15-10-2023
    print(convert_date_format("2000-01-01"))  # Output: 01-01-2000
    print(convert_date_format("1999-12-31"))  # Output: 31-12-1999
    print(convert_date_format("2024-04-09"))  # Output: 09-04-2024