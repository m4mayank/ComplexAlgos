#!/usr/local/bin/python3.7
import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j = j-1
        arr[j]=key
    return arr


l = [100,95,93,92,91,90,89,20,10]
#l = [10,20,89,90,91,92,93,95,100]
print(l)
start_time = time.time()
new_l = insertion_sort(l)
end_time = time.time()
time_taken = (end_time - start_time)*1000000
print(new_l)
print(f"\ntime taken: {time_taken}")
