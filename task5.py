def count_lines_in_text(text):
    if not text.strip():
        return 0
    lines = text.split('\n')
    return len(lines)
if __name__ == "__main__":
    print("Text Line Counter")
    print("=" * 30)
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":  # Empty line means end of input
            break
        lines.append(line)
    text = '\n'.join(lines)
    line_count = count_lines_in_text(text)
    print("\n" + "=" * 30)
    print(f"Your text contains {line_count} lines:")
    print("-" * 30)
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line}")
    print("=" * 30)
