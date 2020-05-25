#!/usr/local/bin/python3.7

#Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.
#
#If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.
#
#Note:
#1. The replacement must be in-place, do **not** allocate extra memory.
#2. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.
#
#Input Format:
#
#    The first and the only argument of input has an array of integers, A.
#
#Output Format:
#    Return an array of integers, representing the next permutation of the given array.
#
#Examples:
#
#Input 1:
#    A = [1, 2, 3]
#
#Output 1:
#        [1, 3, 2]
#
#Input 2:
#    A = [3, 2, 1]
#
#Output 2:
#        [1, 2, 3]
#
#Input 3:
#    A = [1, 1, 5]
#
#Output 3:
#        [1, 5, 1]
#
#Input 4:
#    A = [20, 50, 113]
#
#Output 4:
#        [20, 113, 50]
#

def nextPermutation(A):
    initial_index = (len(A)-1)
    untouched = 1
    if len(A) == 1:
        return A
    got_affected=0
    for i in range(len(A)-2,-1,-1):
        diff = A[initial_index] - A[i]
        if diff > 0:
            untouched = 0
            new_list  =  sorted(A[i:])
            for j in new_list:
                if j > A[i]:
                    A[i] = j
                    got_affected = 1
                    #break
                else:
                    pass

                if got_affected==1:
                    new_list.remove(j)
                    A = A[:i+1]+new_list
                    break
        if got_affected:
            break
        initial_index = i
    if untouched:
        A = sorted(A)
    return A

#A = [1, 2, 3]
#A = [3, 2, 1]
#A=[300, 259, 359, 639, 268, 271, 565, 113, 322, 293, 994, 357, 178, 986, 101, 70, 554, 119, 508, 671, 111, 120, 169, 505, 709, 206, 625, 933, 865, 536, 647, 150, 412, 481, 796, 365, 721, 334, 221, 339, 544, 136, 332, 672, 781, 317, 529, 729, 874, 983, 296, 973, 563, 244, 802, 104, 179, 556, 782, 315, 278, 542, 252, 369, 917, 233, 58, 245, 627, 833, 424, 444, 658, 373, 859, 985, 471, 846, 511, 521, 673, 20, 299, 476]
#A=[319,695,52]
#A=[769, 533]
#A=[ 444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675, 424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16, 158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626, 916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335, 205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311, 164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52 ]
#A=[ 626, 436, 819, 100, 382, 173, 817, 581, 220, 95, 814, 660, 397, 852, 15, 532, 564, 715, 179, 872, 236, 790, 223, 379, 83, 924, 454, 846, 742, 730, 689, 112, 110, 516, 85, 149, 228, 202, 988, 212, 69, 602, 887, 445, 327, 527, 347, 906, 54, 460, 517, 376, 395, 494, 827, 448, 919, 799, 133, 879, 709, 184, 812, 514, 976, 700, 156, 568, 453, 267, 547, 8, 951, 326, 652, 772, 213, 714, 706, 972, 318, 768, 506, 59, 854, 422 ]
#A=[ 839, 776, 843, 422, 252, 385, 543, 94, 711, 636, 517, 257, 222 ]
#A=[59,854,422]
A=[ 251, 844, 767, 778, 658, 337, 10, 252, 632, 262, 707, 506, 701, 475, 410, 696, 631, 903, 516, 149, 344, 101, 42, 891, 991 ]
print(nextPermutation(A))




