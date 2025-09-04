import string

def is_sentence_palindrome(sentence):
    # Remove punctuation and spaces, convert to lowercase
    translator = str.maketrans('', '', string.punctuation + " ")
    cleaned = sentence.translate(translator).lower()
    return cleaned == cleaned[::-1]

# List of test cases
test_cases = [
    ("A man, a plan, a canal, Panama", True),
    ("madam", True),
    ("RaceCar", True),
    ("Was it a car or a cat I saw?", True),
    ("Hello, World!", False),
    ("", True),
    ("     ", True),
    ("!!!", True),
    ("x", True),
    ("abc", False),
    ("@#@!", True),
    ("12321", True),
    ("12345", False),
]

# Run tests
for sentence, expected in test_cases:
    result = is_sentence_palindrome(sentence)
    print(f"Input: {sentence}\nExpected: {expected}, Got: {result}\n")