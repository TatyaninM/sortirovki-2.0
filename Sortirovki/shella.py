import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print("Nor sorted:") 
print(arr)
print("-----")

#step = len(arr) // 2
#while step > 0:
#    for i in range(step, n, 1):
#        value = arr[i]
#        current_index = i
#        index_to_check = current_index - step
#        while current_index > 0 and arr[index_to_check] > value:
#            arr[current_index] = arr[index_to_check]
#            current_index -= step
#            index_to_check -= step
#    step = step // 2     

step = len(arr) // 2
while step > 0:
    for i in range(step, n, 1):
        #value = arr[i]
        current_index = i
        index_to_check = current_index - step
        while (current_index > 0 and 
              arr[index_to_check] > arr[current_index]):
            temp = arr[current_index]
            arr[current_index] = arr[index_to_check]
            current_index -= step
            index_to_check -= step
    step = step // 2       


print("sorted:")    
print(arr)            