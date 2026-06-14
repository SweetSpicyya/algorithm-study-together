class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        curr_start, curr_end = intervals[0]
        output =[]

        for i in range(1,len(intervals)):
            next_start, next_end = intervals[i]
            if next_start<= curr_end:
                curr_end = max(curr_end,next_end)
            elif next_start>curr_end or curr_end>next_end:
                output.append([curr_start,curr_end])
                curr_start = next_start
                curr_end = next_end
        
        output.append([curr_start,curr_end])

        return output

