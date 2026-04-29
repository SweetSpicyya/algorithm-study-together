# {542}. {01 Matrix}

**Link:** https://leetcode.com/problems/01-matrix/description/

**Difficulty:** Medium

**Topic:** Array, Dynamic Programming, Breadth-First Search, Matrix

## Problem Summary
Return the distance of the nearest 0 for each cell

## Approaches & Discussion
### Angela

- **So the problem is asking me to** return the distance of the nearest 0 for each cell.
- **The brute force way could be** to traverse every cell and save the distance **which runs in** O(m^2n^2)(m squared times n squared),**but this is wasteful since** this approach repeatedly traverses the same cells.
- **We can optimize this by** using BFS, **reducing it to** O(mn).
- **My approach is to** use BFS to traverse every cell and calculate the distance of the nearest 0 iteratively. The first step is to add all 0 cells to the queue simultaneously and start BFS from all 0 cells at once. While in the queue, after popping from the queue and traverses current cell's neighbor cells. Each neighboring cell's distance is updated as current distance+1. Lastly return the distance array.
- **This runs in** O(mn) **time complexity** because this approach traverses all the cells in the mn matrix and O(mn) **space complexity since** the result array can grow up to the length of the matrix

