# {994}. {Rotting Oranges}

**Link:** https://leetcode.com/problems/rotting-oranges
**Difficulty:** Medium
**Topic:** Staff, Array, Breadth-First Search, Matrix, Weekly Contest 124

## Problem Summary
return the minimum number of minutes that must elapse until no cell has a fresh orange.

## Approaches & Discussion
### Yourim
Goal: Find the minimum minutes required to rot all fresh oranges, where rot spreads simultaneously in four directions.
The Flaw of Loops: A sequential nested loop causes a cascade effect where an orange rots and immediately infects its neighbor within the same minute pass.
The Solution: Use a Queue to process all currently rotten oranges simultaneously, advancing the timer layer-by-layer.
Initialization: Scan the grid first to count all fresh oranges and push all initial rotten orange coordinates into the queue.
Pop a rotten orange, check its 4 neighbors, turn fresh oranges into rotten ones, and push them into the queue for the next minute.
Termination: Return the total minutes if the fresh orange count reaches zero. otherwise, return -1 if any isolated fresh oranges remain.
Complexity: Both time and space complexities are O(MXN) because every cell is visited a constant number of times.

## Approaches & Discussion
### Angela

- **So this problem is asking me to** return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
- Since we must visit every cell at least once, O(m*n) is already optimal.
- Now, Let's look at the code which I implemented.
- **My approach is to** use queue by using BFS. At first, find all rotten oranges in the matrix and append to queue and find all fresh oranges in the matrix and count. Next, while iterating over the queue, pop all cells at the same level and check their left, right, top, bottom cells whether they are fresh or not. If it is fresh, decrement the fresh count and change the state and append to the queue also using a flag variable to track whether any orange rotted during the current minute, so we know when a minute has elapsed. After this process, if the flag is True, increment the time variable. Lastly, if the fresh oranges still exist, return -1 otherwise return the time

## Approaches & Discussion
### Rachel
- **Understand**: We're given a grid with empty cells (0), fresh oranges (1), and rotten oranges (2). Every minute, rotten oranges spread to adjacent fresh oranges in 4 directions simultaneously.
- **Match**: This is a multi-source BFS problem. Instead of starting from one source, we start from all rotten oranges at once. Each BFS level represents one minute passing.
- **Plan**: First I scan the grid to push all rotten oranges into the queue and count fresh oranges. Then I run BFS level by level. For each rotten orange, I check 4 directions and rot any adjacent fresh orange and adding it to the queue. After BFS, if fresh is still greater than 0, some oranges were unreachable so I return -1.
- **Evaluate**:
  Time: O(m*n) - every cell is visited at most once
  Space: O(m*n) - queue can hold all cells in the worst case
