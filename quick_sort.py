# importing for run time calculation

import sys
import time
sys.setrecursionlimit(150000)
# Creating an array with input from user
arry = [i for i in range(3500)]
# Print array entered by the user
print(" PROVIDED ARRAY: ", arry)

# Defining the start time to measure time required by program.

# split function takes last element as pivot which is placed in the correct position in sorted array,
# & places all smaller than pivot to left of pivot and all greater elements to right of pivot

start = time.time()
def split(arry, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arry[high]  # pivot

    for j in range(low, high):

        # If element is <= to pivot
        if arry[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arry[i], arry[j] = arry[j], arry[i]

    arry[i + 1], arry[high] = arry[high], arry[i + 1]
    return i + 1

# main function to do Quick sort
# arry[]: Array to be sorted, low: Start index, high: End index.


def quicksort(arry, low, high):
    if low < high:
        # sp is partitioning index, arry[p] is now at right place
        sp = split(arry, low, high)

        # Individually sort elements before partition and after partition
        quicksort(arry, low, sp - 1)
        quicksort(arry, sp + 1, high)


n = len(arry)
# Running the quicksort function for entered arry[]

quicksort(arry, 0, n-1)
print("Sorted array:")
for i in range(n):
    print("%d" % arry[i]),

# Function to return start time and day
end = time.time()
print("Elapsed Time",end - start)

# Function to return program run time




