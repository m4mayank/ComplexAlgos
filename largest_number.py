#!/usr/local/bin/python3.7

#Given a list of non negative integers, arrange them such that they form the largest number.
#
#For example:
#
#    Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#

from functools import cmp_to_key


def largestNumber(A):
    A = map(str, A)
    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
    res = ''.join(sorted(A, key= key, reverse=True))
    res = res.lstrip('0')
    return res if res else '0'
    print(res)

#a=(980, 674, 250, 359, 98, 969, 143, 379, 363, 106, 838, 923, 969, 880, 997, 664, 152, 329, 975, 377, 995, 943, 369, 515, 722, 302, 496, 124, 692, 993, 341, 785, 400, 113, 302, 563, 121, 230, 358, 911, 437, 438, 494, 599, 168, 866, 689, 444, 684, 365, 470, 176, 910, 204, 324, 657, 161, 884, 623, 814, 231, 694, 399, 126, 426)
#a=(0,0,0,0)
#a=(1,)
#a=(949,94)
a=(22,9,3,5,33,43,4)
number = largestNumber(a)
print(number)
