import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print("Nor sorted:") 
print(arr)
print("-----")


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    index_of_strong_elem = random.randint(0, len(arr))
    strong_elem = arr[index_of_strong_elem]
    low = list()
    mid = list()
    high = list()

    for elem in arr:
        if elem == strong_elem:
            mid.append(elem)
        elif elem < strong_elem:
            low.append(elem)
        else:
            high.append(elem)        

    low = quick_sort(low)
    high = quick_sort(high)
    result = low + mid + high
    return result

arr = quick_sort(arr)
print ("Sorted:")
print(arr)       