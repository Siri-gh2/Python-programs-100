# Program to count the number of vowels and consonants in a string

s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
