## to find the factorial of a number

#iterative approach 

n = int(input())
f = 1
for i in range (1,n+1):
  f *= 1
print(f)

#Time Complexity: O(n)
#Space Complexity: O(1)


#recurssion

def findFactorial(n):
  if n == 0 or n == 1:
    return 1
  return n*findFactorial(n-1)

n = int(input())
print(findFactorial(n))

#Time Complexity and Space Complexity : O(n)
