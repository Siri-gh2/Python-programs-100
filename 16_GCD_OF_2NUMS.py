#program to fins gcd of 2 no.s
#Eucledian Algorithm

a = int(input())
b = int(input())

while b != 0:
  a, b = b, a % b

print(a)
