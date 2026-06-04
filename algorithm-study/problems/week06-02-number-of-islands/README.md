# {200}. {Number of Islands}

**Link:** https://leetcode.com/problems/number-of-islands
**Difficulty:** Medium
**Topic:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem Summary
find the number of islands

## Approaches & Discussion
### Yourim
Goal: To count the total number of distinct islands in a 2D grid, which can be solved by traversing the grid and exploring connected land cells ('1') using Depth First Search (DFS) or Breadth First Search (BFS).
The Flaw: Simply counting the number of '1's in the grid is insufficient. A valid island requires finding a starting land cell and exploring all of its horizontally or vertically adjacent land cells to treat the entire connected cluster as a single, global island.
Recursive Idea: The optimal approach uses a recursive helper function (DFS) that acts like a "paint bucket tool." When a land cell ('1') is found, it sinks the entire island by converting all connected land cells into water ('0') to prevent duplicate visits.
Recursive Steps: Iterate through every cell (r, c) in the 2D grid using nested loops. And If a land cell ('1') is encountered, increment the island counter and trigger the recursive helper function. 
After that, In the helper function, first check the base case, if the coordinates are out of bounds (r < 0, c < 0, r >= rows, c >= cols) or the cell is water ('0'), return immediately.4. 
Otherwise, flip the current cell to '0' and recursively call the function in all four directions, up, down, left, and right.
Complexity: Time Complexity is O(MXN) where M$ is the number of rows and N is the number of columns, because we visit each cell in the grid a constant number of times.

## Approaches & Discussion
### Angela

- So, this problem is asking me to find the number of islands.
- Since we need to visit all elements in the grid at least once, an **$O(M \times N)$ time complexity** is already optimal.
- I will approach this by using Breadth-First Search (BFS). Let me code this up.
- My approach is to initialize a queue and a count variable to store the number of islands. Next, I will iterate over the grid. If the current element is a land (`"1"`), I increment the count, **mark it as visited by changing it to water (`"0"`)**, and append its coordinates to the queue. **While the queue is not empty**, I **dequeue the coordinates** and check its adjacent cells—top, bottom, left, and right. If an adjacent cell is land, I also mark it as water and append it to the queue. Lastly, I return the count.
- This runs in **$O(M \times N)$ time complexity** because this approach visits every element at most once. The space complexity is **$O(\min(M, N))$** in the worst case, because the maximum size of the queue is bounded by the maximum diagonal of the grid.
