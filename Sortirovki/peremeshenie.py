import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print("Nor sorted:") 
print(arr)
print("-----")

left_index = 0
right_index = n - 1
while left_index <= right_index:
    for i in range(left_index, right_index, +1):
        left = arr[i]
        right = arr[i + 1]
        if left < right:   # Порядок возростания "<"; Порядок убывания ">"
            arr[i] = right
            arr[i + 1] = left
    right_index = right_index - 1
    for i in range(right_index, left_index, -1):
        left = arr[i]
        right = arr[i - 1]
        if left < right:
            arr[i] = left
            arr[i - 1] = right  
    left_index += 1        
print("sorted:")
print(arr)                