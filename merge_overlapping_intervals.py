#!/usr/local/bin/python3.7

#Given a collection of intervals, merge all overlapping intervals.
#
#For example:
#
#    Given [1,3],[2,6],[8,10],[15,18],
#
#    return [1,6],[8,10],[15,18].
#
#Make sure the returned intervals are sorted.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x.start)
    final_list = []
    for i in intervals:
        if len(final_list)==0:
            final_list.append(i)
        if len(final_list)!=0:
            if i.start >= final_list[-1].start and i.start <= final_list[-1].end:
                final_list[-1].end=max(final_list[-1].end, i.end)
            elif final_list[-1] == i:
                continue
            else:
                final_list.append(i)
    return final_list

intervals = [Interval(19,20),Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
llist = merge(intervals)
for i in llist:
    print(i.start, end=",")
    print(i.end, end="\n")


