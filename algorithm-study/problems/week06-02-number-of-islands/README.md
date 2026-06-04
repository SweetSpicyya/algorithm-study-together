# {200}. {Number of Islands}

**Link:** https://leetcode.com/problems/number-of-islands/description/

**Difficulty:** Medium

**Topic:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem Summary
find the number of islands

## Approaches & Discussion
### Angela

- So, this problem is asking me to find the number of islands.
- Since we need to visit all elements in the grid at least once, an **$O(M \times N)$ time complexity** is already optimal.
- I will approach this by using Breadth-First Search (BFS). Let me code this up.
- My approach is to initialize a queue and a count variable to store the number of islands. Next, I will iterate over the grid. If the current element is a land (`"1"`), I increment the count, **mark it as visited by changing it to water (`"0"`)**, and append its coordinates to the queue. **While the queue is not empty**, I **dequeue the coordinates** and check its adjacent cells—top, bottom, left, and right. If an adjacent cell is land, I also mark it as water and append it to the queue. Lastly, I return the count.
- This runs in **$O(M \times N)$ time complexity** because this approach visits every element at most once. The space complexity is **$O(\min(M, N))$** in the worst case, because the maximum size of the queue is bounded by the maximum diagonal of the grid.