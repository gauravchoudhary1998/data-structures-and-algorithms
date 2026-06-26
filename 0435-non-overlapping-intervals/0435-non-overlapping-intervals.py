class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) 
        arrow_pos = intervals[0][1]
        count = 1 
        for i in range(1, len(intervals)): 
            if intervals[i][0] >= arrow_pos: 
                count += 1
                arrow_pos = intervals[i][1]
            # overlap case: do nothing, arrow_pos stays!
    
        return len(intervals) - count