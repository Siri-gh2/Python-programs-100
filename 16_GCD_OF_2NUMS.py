#program to fins gcd of 2 no.s

a = int(input())
b = int(input())

while b != 0:
  a, b = b, a % b

print(a)
