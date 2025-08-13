# ZERO-SHOT APPROACH - Basic implementation
def count_vowels_zero_shot(text):
    """
    Basic vowel counting function (zero-shot approach)
    """
    count = 0
    for char in text:
        if char.lower() in 'aeiou':
            count += 1
    return count

# FEW-SHOT APPROACH - More robust implementation
def count_vowels_few_shot(text):
    """
    Robust vowel counting function (few-shot approach)
    - Handles case sensitivity
    - Includes input validation
    - More comprehensive vowel set
    """
    if not isinstance(text, str):
        return 0
    
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


# Example usage and demonstration
if __name__ == "__main__":
    # Test cases
    test_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU",
        "Rhythm",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    print("COMPARISON: Zero-shot vs Few-shot Approaches")
    print("=" * 60)
    print(f"{'Input String':<30} {'Zero-shot':<12} {'Few-shot':<12}")
    print("-" * 60)
    
    for test_string in test_strings:
        zero_shot_result = count_vowels_zero_shot(test_string)
        few_shot_result = count_vowels_few_shot(test_string)
        print(f"'{test_string:<28}' {zero_shot_result:<12} {few_shot_result:<12}")
    
    print("\n" + "=" * 60)
    print("KEY DIFFERENCES IN OUTPUT:")
    print("1. Zero-shot: Uses .lower() method, simpler logic")
    print("2. Few-shot: Handles both cases, includes validation")
    print("3. Both approaches give same results for valid strings")
    
    print("\n" + "=" * 60)
    
    # Interactive input comparison
    user_input = input("Enter a string to compare both approaches: ")
    zero_shot_result = count_vowels_zero_shot(user_input)
    few_shot_result = count_vowels_few_shot(user_input)
    
    print(f"\nResults for '{user_input}':")
    print(f"Zero-shot approach: {zero_shot_result} vowels")
    print(f"Few-shot approach:  {few_shot_result} vowels")


"""
COMPARISON: Zero-shot vs Few-shot Prompting

ZERO-SHOT PROMPT:
"Write a function that counts the number of vowels in a string"

FEW-SHOT PROMPT:
"Write a function that counts the number of vowels in a string.

Examples:
Input: 'hello' → Output: 2
Input: 'world' → Output: 1  
Input: 'python' → Output: 1
Input: 'aeiou' → Output: 5

The function should:
- Take a string as input
- Count all vowels (a, e, i, o, u) regardless of case
- Return the total count as an integer"

ADVANTAGES OF FEW-SHOT:
1. Clearer understanding of expected input/output format
2. Better handling of edge cases (like case sensitivity)
3. More consistent function structure
4. Reduced ambiguity about requirements

ADVANTAGES OF ZERO-SHOT:
1. More creative solutions
2. Less biased toward specific implementation
3. Faster to write
4. May discover novel approaches
"""
