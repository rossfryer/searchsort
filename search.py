import random
import time

def generate_list(length):
    list = []
    for i in range (0,length):
        item = random.randint(0,length-1)
        list.append(item)
    return list

def linear_search(arr, target):
    start = time.time()
    found = False
    pos = 0
    while found == False and pos < len(arr):
        if arr[pos] == target:
            found = True
            break
        else:
            pos = pos + 1
    end = time.time()
    print(f"Time taken for linear search: {end - start}")
    return (pos, found)

def binary_search(arr, target):
    start = time.time()
    low = 0
    high = len(arr)-1
    found = False
    pos = -1
    while found == False and low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            found = True
            pos = mid
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    end = time.time()
    print(f"Time taken for binary search: {end - start}")
    return (pos, found)

num = int(input("Enter the number of elements in the list: "))
list = generate_list(num)

target = int(input("Enter the number to be searched in the list: "))
pos, found = linear_search(list, target)
list.sort()
pos, found = binary_search(list, target)

if found == True:
    print(f"Element is present in the list at {pos}")
else:
    print(f"Element is not present in the list")
