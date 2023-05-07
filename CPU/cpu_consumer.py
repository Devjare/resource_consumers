import numpy as np
import random
import sys

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

    return arr

n = int(sys.argv[1])
i = 0
while True:
    print(f"Iteration #{i} applying bubble sort to array of size {n}.")
    arr = bubble_sort(np.random.randint(1,1000,n))
    i += 1
