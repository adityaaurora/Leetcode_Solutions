#selection sort practice
arr = [1, 6, 8, 2, 5, 9]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i #initialize the first minimum index
        for j in range(i + 1, len(arr)): #j is the range from the second element after the min_index to the last element of the array
            if arr[j] < arr[min_idx]:
                min_idx = j #change min index to the minimum item found in the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort(arr)
print(arr)
