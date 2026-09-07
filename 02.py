import string

text = input("Enter a sentence or paragraph: ")

text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

print("\nTotal words:", len(words))

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

print("\nPalindromes:")

found = False

for word in frequency:
    if word == word[::-1] and len(word) > 1:
        print(word)
        found = True

if not found:
    print("No palindrome found")
