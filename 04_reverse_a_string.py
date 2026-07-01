#reversing a string without using method reverse()

#slicing

s = input()
print("reverse of the string s is:",s[::-1])

#time and space complexity is O(n)


#without slicing

s = input()
rev = ""

for ch in s:
  rev = ch + rev

print(rev)

# time complexity = o(n^2)

# Reverse a string without using slicing

s = input("Enter a string: ")

rev = ""

for i in range(len(s) - 1, -1, -1):
    rev += s[i]

print("Reversed string:", rev)

#Time Complexity: O(n²) (because of repeated string concatenation)
#Space Complexity: O(n)

#most efficient implementation without slicing

chars = []

for i in range(len(s) - 1, -1, -1):
    chars.append(s[i])

print("".join(chars))

#Time Complexity: O(n)
#Space Complexity: O(n)

