import re
import pytest

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9-]+', ' ', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text

@pytest.mark.parametrize("input_text, expected", [
    ("Hello World!", "hello-world"),
    ("AI & You", "ai-you"),
    ("Set13-C2", "set13-c2"),
    ("   Leading and trailing   ", "leading-and-trailing"),
    ("Multiple   Spaces", "multiple-spaces"),
    ("Hello---World", "hello-world"),
    ("!!!OnlyPunct!!!", "onlypunct"),
    ("----Already--slugified----", "already-slugified"),
    ("", ""),
])
def test_slugify(input_text, expected):
    assert slugify(input_text) == expected
if __name__ == "__main__":
    sample = input("Enter titles separated by commas: ").split(",")
    print([slugify(s.strip()) for s in sample])
