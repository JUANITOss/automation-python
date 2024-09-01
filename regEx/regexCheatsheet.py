# regex_cheatsheet.py

import re

def display_match(pattern, text):
    match = re.search(pattern, text)
    return match.group() if match else "No match"

# Regex Cheatsheet

cheatsheet = {
    "Match any character": r".",
    "Match start of string": r"^start",
    "Match end of string": r"end$",
    "Match zero or more repetitions": r"a*",
    "Match one or more repetitions": r"a+",
    "Match zero or one repetition": r"a?",
    "Match exactly n repetitions": r"a{2}",
    "Match n or more repetitions": r"a{2,}",
    "Match between n and m repetitions": r"a{2,4}",
    "Match any of the characters in set": r"[abc]",
    "Match any character not in set": r"[^abc]",
    "Match either a or b": r"a|b",
    "Escape special characters": r"\.",
    "Match word boundary": r"\bword\b",
    "Match non-word boundary": r"\Bword\B",
    "Match digit": r"\d",
    "Match non-digit": r"\D",
    "Match whitespace": r"\s",
    "Match non-whitespace": r"\S",
    "Match word character": r"\w",
    "Match non-word character": r"\W",
}

# Example Texts
text_examples = {
    "Example with a digit": "abc123xyz",
    "Example with whitespace": "hello world",
    "Example with word boundary": "word in the text",
    "Example with exact match": "start and end",
    "Example with repetitions": "aaabbbbccccc",
    "Example with character set": "a1b2c3",
}

# Display Results
print("Regex Cheatsheet with Examples:\n")

for desc, pattern in cheatsheet.items():
    print(f"{desc}:")
    for example_desc, text in text_examples.items():
        print(f"  {example_desc}:")
        result = display_match(pattern, text)
        print(f"    Pattern: {pattern}")
        print(f"    Text: '{text}'")
        print(f"    Match: {result}\n")
