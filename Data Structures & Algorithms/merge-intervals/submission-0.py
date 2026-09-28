class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #im thinking two pointers, l and r, where l = 0 and r = 1, we want to check if l[0] <= r[0] <= l[1] = overlapping, r[0] <= l[1] <= r[1] = overlapping
        #base case
        if len(intervals) <= 1:
            return intervals

        l, r = 0, 1
        res = []

        intervals.sort()

        while r < len(intervals): # O(n)
            #things to consider:
                #when do we incremement l?
                    #r[0] > l[1]
            #assumption: list of intervals is sorted

            if intervals[l][1] < intervals[r][0]:
                res.append(intervals[l])  
                l = r

            else:
                intervals[l][1] = max(intervals[r][1], intervals[l][1]) #new interval to consider before we append anything

            r += 1
            
        if r >= len(intervals):
            res.append(intervals[l])
        
        return res

                
