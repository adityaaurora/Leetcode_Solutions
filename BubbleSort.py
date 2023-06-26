def bubble(arr):
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
    
list = [5, 1, 9, 3, 2, 7, 4]
bubble(list)
print(list)
