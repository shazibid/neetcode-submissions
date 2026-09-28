class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #need to remove MIN number of intervals to make all intervals NONOVERLAPPING

        intervals.sort()

        count = 0
        tempEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= tempEnd:
                tempEnd = end
            else:
                count += 1
                tempEnd = min(tempEnd, end)

            

        return count