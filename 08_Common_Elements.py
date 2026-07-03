# Program to find the common elements between two lists

list1 = list(map(int, input("Enter elements of List 1: ").split()))
list2 = list(map(int, input("Enter elements of List 2: ").split()))

set1 = set(list1)
common = []

for num in list2:
    if num in set1 and num not in common:
        common.append(num)

if common:
    print("Common elements:", common)
else:
    print("No common elements found.")


# Program to find the common elements between two lists

list1 = list(map(int, input("Enter elements of List 1: ").split()))
list2 = list(map(int, input("Enter elements of List 2: ").split()))

common = list(set(list1).intersection(set(list2)))

if common:
    print("Common elements:", common)
else:
    print("No common elements found.")

