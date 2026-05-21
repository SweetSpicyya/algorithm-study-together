# {207}. {Course Schedule}

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