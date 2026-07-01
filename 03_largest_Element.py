# to find the largest no. in the given array of inputs

arr = list(map(int, input().split()))
l = arr[0]

for i in arr:
  if i > l:
    l = i

print(l)
