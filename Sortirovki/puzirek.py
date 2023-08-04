import random

n = 500
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
print("Nor sorted:") 
print(arr)
print("-----")

for i in range(n):
    for j in range(n - 1):
        #left = arr[j]
       # right = arr[j + 1]
        #if left < right:
            #arr[j] = right
            #arr[j + 1] = left
        if arr [j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr [j + 1]
            arr [j + 1] = temp



print("sorted:")    
print(arr)       