# Program to remove duplicates from a list

arr = list(map(int, input("Enter the elements: ").split()))

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)


# Program to remove duplicates using set

arr = list(map(int, input("Enter the elements: ").split()))

unique = list(set(arr))

print("List after removing duplicates:", unique)

# Program to remove duplicates while preserving order

arr = list(map(int, input("Enter the elements: ").split()))

unique = list(dict.fromkeys(arr))

print("List after removing duplicates:", unique)



#Complexities 

| Approach                      | Time      | Space    | Preserves Order |
| ----------------------------- | --------- | -------- | --------------- |
| List (`if num not in unique`) | **O(n²)** | **O(n)** | ✅ Yes          |
| `set()`                       | **O(n)**  | **O(n)** | ❌ No           |
| `dict.fromkeys()`             | **O(n)**  | **O(n)** | ✅ Yes ⭐       |

