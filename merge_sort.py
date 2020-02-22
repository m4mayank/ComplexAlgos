#!/usr/local/bin/python3.7

#Function to merge the lists
def comp_merge(lst1, lst2):
    i=0
    j=0
    k=0
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)
    total_length = len_lst1 + len_lst2
    temp =[0] * total_length

    while (i < len_lst1) and (j < len_lst2):
        if lst1[i] <= lst2[j]:
            temp[k] = lst1[i]
            i += 1
            k += 1
        else:
            temp[k] = lst2[j]
            j += 1
            k += 1

    while j < len_lst2:
        temp[k] = lst2[j]
        k += 1
        j += 1

    while i < len_lst1:
        temp[k] = lst1[i]
        k+=1
        i+=1

    return temp



#Function to break the list into two parts recursively
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        first_half = [arr[i] for i in range(0,mid)]
        second_half = [arr[i] for i in range(mid, len(arr))]
        first_sorted = merge_sort(first_half)
        second_sorted = merge_sort(second_half)
        srted_list = comp_merge(first_sorted, second_sorted)
        return srted_list
    else:
        return arr

unsorted_lst=[95,12,187,76,557,32,10,98]
sorted_list = merge_sort(unsorted_lst)
print(sorted_list)
