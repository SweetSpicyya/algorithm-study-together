# {207}. {Course Schedule}

**Link:** https://leetcode.com/problems/course-schedule/
**Difficulty:** Medium
**Topic:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort

## Approaches & Discussion

### Rachel

- **Understand**: We're given a number of courses and a list of prerequisites where [a,b] means you must take course b before course a. We need to return true if all courses can be finished, false otherwise. The key insight is that if there's a cycle in the prerequisites, it's impossible to finish all courses.
- **Match**:This is a cycle detection problem on a directed graph. I'll use DFS with a state array to track three states per node: unvisited(0), currently being explored(1), and fully explored(2). If we encounter a node with state 1 during DFS, we've found a cycle.
- **Plan**: First I'll build an adjacency list from the prerequisites array. Then I'll run DFS on every course. Each DFS marks the current course as state 1, recursively visites all next courses, and marks it state 2 when done. If we ever visit a course that's already state 1, there's a cycle and we return false.
- **Evaluate**: Time complexity is O(V+E) since every node and edge is visited exactly once. Space complexity is O(V+E), adgacency list stores all edges, state array stores all nodes, call stack goes as deep as the longest path.
