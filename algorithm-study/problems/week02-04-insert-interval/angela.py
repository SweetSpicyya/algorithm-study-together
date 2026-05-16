class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # result = []
        # flag = False
        # count = 0

        # if len(intervals) == 0:
        #     result.append(newInterval)
        #     return result
        # elif newInterval[1] < intervals[0][0]:
        #     result.append(newInterval)
        #     for current in intervals:
        #         result.append(current)
        #     return result
        # elif newInterval[0] > intervals[len(intervals)-1][1]:
        #     for current in intervals:
        #         result.append(current)
        #     result.append(newInterval)
        #     return result
        # else:
        #     for current in intervals:
        #         if newInterval[1] < current[0]:
        #             if flag == True:
        #                 result.append(newInterval)
        #                 flag = False
        #             elif flag==False and count==0:
        #                 result.append(newInterval)
        #                 count+=1
        #             result.append(current)
        #         elif newInterval[0] > current[1]:
        #             result.append(current)
        #         else:
        #             newInterval[0] = min(newInterval[0],current[0])
        #             newInterval[1] = max(newInterval[1], current[1])
        #             flag = True
        #             count+=1
            
        #     if len(result)==0 or flag==True:
        #         result.append(newInterval)
                
        # return result  

        #Shorter way
        result = []

        for current in intervals:
            if newInterval[1] < current[0]:
                result.append(newInterval)
                newInterval=current
            elif newInterval[0] > current[1]:
                result.append(current)
            else:
                newInterval[0] = min(newInterval[0],current[0])
                newInterval[1] = max(newInterval[1],current[1])
        
        result.append(newInterval)
        return result