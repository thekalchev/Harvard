text = input("Input: ")
vowels = "AEIOUaeiou"

text_without_vowels = ""

for char in text:
    if char not in vowels:
        text_without_vowels += char


print(f"Output: {text_without_vowels}")