import heapq
from typing import List
import math

class Solution:
    def kClosest_naive(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_distance_array = []
        i = 0
        while i < len(points):
            current_distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            sorted_distance_array.append((current_distance, [points[i][0], points[i][1]]))

            i += 1

        sorted_distance_array.sort()
        print(sorted_distance_array)

        k_array = []
        i_k = 0
        while i_k < k:
            d, c = sorted_distance_array[i_k]
            k_array.append(c)
            i_k += 1

        print(k_array)

    def kClosest (self, points: List[List[int]], k: int) -> List[List[int]]:
        max_head = []

        for x, y in points:
            dist_sq = -(x**2 + y**2)

            if len(max_head) < k:
                heapq.heappush(max_head, (dist_sq,[x, y]))
            else:
                heapq.heappushpop(max_head, (dist_sq,[x, y]))

        print(c for d, c in max_head)

s = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
s.kClosest(points, k)