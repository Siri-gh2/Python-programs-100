# Program to find the union and intersection of two sets

set1 = set(map(int, input("Enter elements of Set 1: ").split()))
set2 = set(map(int, input("Enter elements of Set 2: ").split()))

union = set1 | set2
intersection = set1 & set2

print("Union:", union)
print("Intersection:", intersection)
