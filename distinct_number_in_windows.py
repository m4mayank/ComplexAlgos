#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
def dNums(A, B):
    final_list = []
    dicti = {}
    counter = 0
    for i in range(0, len(A)):
        if A[i] in dicti:
            dicti[A[i]] = dicti[A[i]] + 1
        else:
            dicti[A[i]] = 1
        counter += 1 
        if counter == B:
            counter = counter - 1
            final_list.append(len(dicti))
            key = A[i-(B-1)]
            dicti[key] = dicti[key]-1
            if dicti[key] == 0:
                del dicti[key]
    return final_list

#A = [1, 2, 1, 3, 4, 3]
#B = 3
A = [1, 1, 2, 2]
B = 1
llist = dNums(A, B)
print(llist)