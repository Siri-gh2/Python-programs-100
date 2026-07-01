#count the frequency of each element in a list


arr = list(map(input().split()))
freq = {}

for num in arr:
  if num in freq:
    freq[num] += 1
  else:
    freq[num] = 1

print(freq)



## Time and Space Complexity is O(n)
