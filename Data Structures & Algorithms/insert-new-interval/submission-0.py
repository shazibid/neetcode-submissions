class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #if no overlap (ie, one value isnt between an existing interval) then return the existing set of intervals with the new one positioned sorted into the list

        res = []

        for i in range(len(intervals)): #O(n)
            #O(1), ensures both values of interval are outside of the overlapping region
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval) #O(1)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res

            

            

