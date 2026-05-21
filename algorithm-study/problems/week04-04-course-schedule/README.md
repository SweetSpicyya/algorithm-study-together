# {207}. {Course Schedule}

**Link:** https://leetcode.com/problems/course-schedule/

**Difficulty:** Medium

**Topic:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort

## Problem Summary
determine whether we can finish all given courses or not.

## Approaches & Discussion
### Angela

- **So this problem is asking me to** determine whether we can finish all given courses or not.
- **We should** traverse all courses, so O(V+E) is already optimal.
- **I will approach this by** using graph, dfs and hashmap to solve the problem.
- **Now, Let me code this up.**
- **My approach is to** make adjacency list by using hashmap and make array to store states of the courses. Next, in the dfs function, if the course's state is 1, it means a cycle exists so return False. If the state is 2, it means it has already been verified the logic so return True otherwise, change the state to 1 and traverse the courses which relate to the current course using recursive call. if the result is False, return False otherwise change the state to 2 since no cycle was detected and return True. Lastly iterate over all given courses, return False if any cycle is detected, otherwise return True
- **This runs in** O(V+E) time complexity because this approach traverses all graph's nodes and edges and O(V+E) space complexity since the call stack and adjacency list can grow up to O(V+E)