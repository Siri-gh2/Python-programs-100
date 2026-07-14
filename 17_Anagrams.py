#anagrams - same characters with the same frequency, can be of different order


s# Program to check whether two strings are anagrams

s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    if freq1 == freq2:
        print("Anagram")
    else:
        print("Not Anagram")
