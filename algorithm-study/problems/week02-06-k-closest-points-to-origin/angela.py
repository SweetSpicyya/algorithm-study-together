import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # O(nlogn) - min heap
        #heap = []

        #for x in range(len(points)):
            #dis =points[x][0]**2+points[x][1]**2
            #point = [points[x][0],points[x][1]]
            #heapq.heappush(heap,(dis,point))
        
        #result = []
        #for i in range(k):
            #dis, point = heapq.heappop(heap)
            #result.append(point)
        
        #return result

        # O(nlogk) - max heap
        heap = []

        for x in range(len(points)):
            dis = points[x][0]**2 + points[x][1]**2
            point = [points[x][0], points[x][1]]
            heapq.heappush(heap,(-dis,point))

            if len(heap) > k :
                heapq.heappop(heap)
        
        return [point for dis, point in heap]
        # result = []
        # for dis, point in heap:
        #   result.append(point)
        # return result