import sys

def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


# Command-line arguments
text = sys.argv[1]
shift = int(sys.argv[2])

print("Original message:", text)
print("Shift key:", shift)
print("Encrypted message:", caesar_cipher(text, shift))
