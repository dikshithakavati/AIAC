def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    filename = "file1.txt"
    try:
        content = read_file(filename)
        print(content)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
    except OSError as e:
        print(f"Error reading '{filename}': {e}")