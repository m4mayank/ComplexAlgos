#!/usr/local/bin/python3.7

#Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
#You may assume that the intervals were initially sorted according to their start times.
#
#Example 1:
#
#    Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
#
#Example 2:
#
#    Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
#
#This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#
#Make sure the returned intervals are also sorted.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(intervals, new_interval):
    final_array = []
    interval_array=[]
    count = 0
    if new_interval.start > intervals[-1].end:
        if intervals[0].start == 0 and intervals[0].end == 0:
            intervals.clear()
            intervals.append(new_interval)
            return intervals
        intervals.append(new_interval)
        return intervals

    for i in range(0,len(intervals)):
        if new_interval.start < intervals[i].start:
                interval_array.append(new_interval.start)
                count = i
                break

        if new_interval.start >= intervals[i].start and new_interval.start <= intervals[i].end:
            interval_array.append(intervals[i].start)
            count=i
            break

        final_array.append(intervals[i])

    if new_interval.end > intervals[-1].end:
        interval_array.append(new_interval.end)
        final_array.append(Interval(interval_array[0], interval_array[1]))
        return final_array


    for i in range(count, len(intervals)):
        if new_interval.end < intervals[i].start:
            interval_array.append(new_interval.end)
            count = i
            break

        if new_interval.end <= intervals[i].end:
            interval_array.append(intervals[i].end)
            count = i+1
            break

    final_array.append(Interval(interval_array[0], interval_array[1]))
    if count < len(intervals):
        for i in range(count, len(intervals)):
            final_array.append(intervals[i])

    return final_array




#intervals = [Interval(4,5),Interval(8,10),Interval(12,16)]
#intervals = [ Interval(6037774, 6198243), Interval(6726550, 7004541), Interval(8842554, 10866536), Interval(11027721, 11341296), Interval(11972532, 14746848), Interval(16374805, 16706396), Interval(17557262, 20518214), Interval(22139780, 22379559), Interval(27212352, 28404611), Interval(28921768, 29621583), Interval(29823256, 32060921), Interval(33950165, 36418956), Interval(37225039, 37785557), Interval(40087908, 41184444), Interval(41922814, 45297414), Interval(48142402, 48244133), Interval(48622983, 50443163), Interval(50898369, 55612831), Interval(57030757, 58120901), Interval(59772759, 59943999), Interval(61141939, 64859907), Interval(65277782, 65296274), Interval(67497842, 68386607), Interval(70414085, 73339545), Interval(73896106, 75605861), Interval(79672668, 84539434), Interval(84821550, 86558001), Interval(91116470, 92198054), Interval(96147808, 98979097) ]
intervals = [Interval(0,0)]
arr = insert(intervals, Interval(36210193,1000984219))
#arr = insert(intervals, Interval(36210193,1000984219))
#print("New Interval : 36210193,1000984219)")
for i in arr:
    print(i.start, end=",")
    print(i.end, end="\n")
