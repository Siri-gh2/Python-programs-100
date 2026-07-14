#Fibonacci Series

def fib(n):
  if n<1:
    return 0
  return fib(n-1)+fib(n-2)

n = int(input())

for i in range(n):
  print(fib(i),end = " ")
