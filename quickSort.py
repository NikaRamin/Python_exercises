# Quicksort program without error handling

import numpy as np
import time

def quickSort(arr):
    if len(arr)<= 1:
        return arr
    pivot = arr[0]
    right = arr[1:][arr[1:] >= pivot]
    left = arr[1:][arr[1:] < pivot]
    return np.concatenate((quickSort(left),np.array([pivot]),quickSort(right)))

arr = np.random.randint(1,1000000,size=1000000)
start_time = time.time()
result = quickSort(arr)
end_time = time.time()
execution_time = round(end_time - start_time,2)
print(f"Result: {result}\nExecution time: {execution_time}")

