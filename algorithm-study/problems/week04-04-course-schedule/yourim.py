from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses


        for ai, bi in prerequisites:
            adj[bi].append(ai)
            indegree[ai] += 1


        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        visited_count = 0


        while queue:
            curr = queue.popleft()
            visited_count += 1

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return visited_count == numCourses