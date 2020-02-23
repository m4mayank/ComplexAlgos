#!/usr/local/bin/python3.7

unsorted_list=[95,12,187,76,557,32,10,98]

#one function to partition using pivot
def partition(arr, start, end):
    pivot = end
    pindex = start
    for i in range(start, end):
        if arr[i] <= arr[pivot]:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex+=1
    arr[pindex], arr[pivot] = arr[pivot], arr[pindex]
    return pindex

#another fucntion to recursively call the same function
def quick_sort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)
        quick_sort(arr, start, partition_index-1)
        quick_sort(arr, partition_index+1, end)



quick_sort(unsorted_list, 0 , len(unsorted_list)-1)
print(unsorted_list)
