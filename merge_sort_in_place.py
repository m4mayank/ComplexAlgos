#!/usr/local/bin/python3.7

unsorted_lst=[95,12,187,76,557,32,10,98]

#Function to merge the lists
def comp_merge(arr, start, end, mid):
    i=start
    j=mid+1
    k=0
    temp = [0] * len(arr)

    while (i <= mid)  and (j <= end):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1

    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1

    while i <= mid:
        temp[k] = arr[i]
        k+=1
        i+=1

    n = start
    while n <= end:
        arr[n] = temp[n - start]
        n+=1



#Function to break the list into two parts recursively
def merge_sort(arr, start, end):
    if end > start:
        mid = (end+start)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        comp_merge(arr, start, end, mid)

print(unsorted_lst)
start = 0
end = len(unsorted_lst) - 1
merge_sort(unsorted_lst, start, end)
print(unsorted_lst)
