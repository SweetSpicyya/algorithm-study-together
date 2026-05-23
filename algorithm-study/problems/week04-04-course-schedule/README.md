# {207}. {Course Schedule}

<<<<<<< HEAD
**Link:** https://leetcode.com/problems/course-schedule

**Difficulty:** Medium
**Topic:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort

## Problem Summary
determine if all courses can be finished without falling into a deadlock (cycle) caused by prerequisite requirements.


## Approaches & Discussion
### Yourim
We can model this as a directed graph and use topological sort to check for the presence of a cycle.
First, I'll build an adjacency list to map the course dependencies and create an indegree array to track the number of prerequisites for each course.
Then, I'll push all courses with an indegree of 0 into a queue and process them one by one, decrementing the indegree of their neighboring courses.
Finally, if the total number of processed courses equals numCourses, it means all courses can be finished, so we return True; otherwise, there is a cycle, and we return False."

## Approaches & Discussion

### Rachel

- **Understand**: We're given a number of courses and a list of prerequisites where [a,b] means you must take course b before course a. We need to return true if all courses can be finished, false otherwise. The key insight is that if there's a cycle in the prerequisites, it's impossible to finish all courses.
- **Match**:This is a cycle detection problem on a directed graph. I'll use DFS with a state array to track three states per node: unvisited(0), currently being explored(1), and fully explored(2). If we encounter a node with state 1 during DFS, we've found a cycle.
- **Plan**: First I'll build an adjacency list from the prerequisites array. Then I'll run DFS on every course. Each DFS marks the current course as state 1, recursively visites all next courses, and marks it state 2 when done. If we ever visit a course that's already state 1, there's a cycle and we return false.
- **Evaluate**: Time complexity is O(V+E) since every node and edge is visited exactly once. Space complexity is O(V+E), adgacency list stores all edges, state array stores all nodes, call stack goes as deep as the longest path.

## Approaches & Discussion
### Angela

- **So this problem is asking me to** determine whether we can finish all given courses or not.
- **We should** traverse all courses, so O(V+E) is already optimal.
- **I will approach this by** using graph, dfs and hashmap to solve the problem.
- **Now, Let me code this up.**
- **My approach is to** make adjacency list by using hashmap and make array to store states of the courses. Next, in the dfs function, if the course's state is 1, it means a cycle exists so return False. If the state is 2, it means it has already been verified the logic so return True otherwise, change the state to 1 and traverse the courses which relate to the current course using recursive call. if the result is False, return False otherwise change the state to 2 since no cycle was detected and return True. Lastly iterate over all given courses, return False if any cycle is detected, otherwise return True
- **This runs in** O(V+E) time complexity because this approach traverses all graph's nodes and edges and O(V+E) space complexity since the call stack and adjacency list can grow up to O(V+E)
