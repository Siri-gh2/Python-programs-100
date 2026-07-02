# Program to find the second largest element in a list

arr = list(map(int, input("Enter elements: ").split()))

if len(arr) < 2:
    print("Second largest element does not exist")
else:
    largest = float('-inf')
    secondLargest = float('-inf')

    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif largest > num > secondLargest:
            secondLargest = num

    if secondLargest == float('-inf'):
        print("Second largest element does not exist")
    else:
        print("Second largest element:", secondLargest)
