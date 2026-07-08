# Program to remove duplicates from a list

arr = list(map(int, input("Enter the elements: ").split()))

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)
