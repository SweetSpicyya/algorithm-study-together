# {542}. {01 Matrix}

**Link:** https://leetcode.com/problems/01-matrix/
**Difficulty:** Medium
**Topic:** Principal, Array, Dynamic Programming, Breadth-First Search, Matrix

## Problem Summary

Find the distance of the nearest 0 for each cell

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by setting 0 for the cells that is 0, and then searching 4 directions of the 1 while finding 0.
- **Optimization**: Instead of calculating the distance for each 1 individualy, I optimized the solution by using a Multi-source Breadth-First Search. By initiating the BFS from 0, it can propagate the distance incrementally. I initialized all 1s as Infinity to track unvisited cells.


## Approaches & Discussion
### Yourim
- **Coding interview**:
<details>
  <summary>Click to view details </summary>
  
  So the problem is basically for every cell in the matrix, we want to find the distance to nearest zero. 
  And the distance here is just the number of steps like up, down, left, right.
  
  Okay so, I guess the naive approach would be something like we can scan through every single cell.
  If it's a Zero, we just skip it distance is already Zero. But if we hit a one, we run a BFS from that specific cell
  and keep expanding outward until we find a zero, and that's the distance we record for that cell.
  So the time complexity on this. so like we're doing a full BFS for every single one cell and in the worst case that BFS touches the entire matrix.
  that give us O((MXN)^2). That's pretty expensive. We're doing a ton of repeated work, so we need a better approach.

  So the key insight is instead of going from each one to find a zero, what if we just flip it?
  Like, what if we start from all the zeros simultaneously expand outward?

  And, one thing I want to talk about is the marking strategy. So the thing is we need some way to track cells that haven't been visited yet.
  And I'd use -1 for that instead of just leaving them as 1. Because if I keep the value as 1, when I'm doing BFS I can't tell
  is the cell an unvisited one, or is the distance? So making unvisited ones as -1, I guess, keeps things clean and unambiguous.
  
  The setup is we go through the matrix and every zero gets pushed into the queue as-is.
  Every one gets overwritten with -1, just flagged as unvisited.
  Then we run BFS. We pop a cell, check all four neighbors. If a neighbor is -1, we set it to current value plus one.
  That's the distance. Push it into te queue and keep going.
  Because we're expanding layer by layer from all zeros at the same time, the first time we reach any cell is guaranteed to be the shortest path.
  That's just how BFS works.

  So time complexity, it's O(MXN). Every cell gets touched exactly once. Space is also O(MXN) for the queue in the worst case.
  
  Okay so let me work through the code.
  We grab the dimensions and initialize the queue.
  So this is the seeding step. Zeros go straight into the queue. The distance is already zero. And ones get marked -1, so we know they haven't been reached yet.
  Standard BFS. Check bounds, and we only process cells that are still -1.
  When we find one, we assign it current distance plus one and queue it up. And I guess the nice thing here is we're modifying the matrix in-place,
  so we don't need separate result array. And at the end, the matrix holds all the distances. So we just return it.

</details>


## Problem Summary
Return the distance of the nearest 0 for each cell

## Approaches & Discussion
### Angela

- **So the problem is asking me to** return the distance of the nearest 0 for each cell.
- **The brute force way could be** to traverse every cell and save the distance **which runs in** O(m^2n^2)(m squared times n squared),**but this is wasteful since** this approach repeatedly traverses the same cells.
- **We can optimize this by** using BFS, **reducing it to** O(mn).
- **My approach is to** use BFS to traverse every cell and calculate the distance of the nearest 0 iteratively. The first step is to add all 0 cells to the queue simultaneously and start BFS from all 0 cells at once. While in the queue, after popping from the queue and traverses current cell's neighbor cells. Each neighboring cell's distance is updated as current distance+1. Lastly return the distance array.
- **This runs in** O(mn) **time complexity** because this approach traverses all the cells in the mn matrix and O(mn) **space complexity since** the result array can grow up to the length of the matrix

