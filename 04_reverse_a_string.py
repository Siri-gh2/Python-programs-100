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
