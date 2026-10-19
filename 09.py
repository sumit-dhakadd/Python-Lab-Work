# Remove spaces and special characters
def normalize(value):
    result = ""
    for char in value:
        if char.isalnum():
            result += char.lower()
    return result

# Check whether two strings are anagrams
def check_anagram(first, second):
    return sorted(normalize(first)) == sorted(normalize(second))

# Create groups of anagrams
def make_groups(items):
    result = {}

    for item in items:
        key = ''.join(sorted(normalize(item)))
        result.setdefault(key, []).append(item)

    return result

# Get two inputs
first_text = input("Enter first word or phrase: ")
second_text = input("Enter second word or phrase: ")

if check_anagram(first_text, second_text):
    print("The two texts are anagrams.")
else:
    print("The two texts are not anagrams.")

# Group multiple words
words_list = input(
    "\nEnter multiple words separated by spaces: "
).split()

anagram_groups = make_groups(words_list)

print("\nAnagram Groups:")
for group in anagram_groups.values():
    print(group)
