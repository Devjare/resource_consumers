import os
import time
import numpy as np

def bubble_sort(size):
    """
    Function to create a random array of size 'size'
    and sort with bubble sort
    """
    arr = np.random.random(size)
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr

size=10000
start = time.time()
bubble_sort(size=size)
end = time.time()
tt = end - start # In seconds
print(f"Finished sorting array of size {size} in {tt} seconds")
