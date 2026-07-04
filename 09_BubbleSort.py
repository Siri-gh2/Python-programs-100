# Program to sort a list using Bubble Sort

arr = list(map(int, input("Enter the elements: ").split()))

n = len(arr)

for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

print("Sorted list:", arr)
