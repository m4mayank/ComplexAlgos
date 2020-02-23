#!/usr/local/bin/python3.7

unsorted_list=[95,12,187,76,557,32,10,98]


def selection_sort(arr, start, end):
    for i in range(start, end):
        min_index=i
        for j in range(i+1, end+1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i], arr[min_index]

selection_sort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)
