#!/usr/local/bin/python3.7

unsorted_list=[95,12,187,76,557,32,10,98]


def bubble_sort(arr, start, end):
    for i in range (start, end):
        j = start
        while j < end:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j+=1

print(unsorted_list)
bubble_sort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)
