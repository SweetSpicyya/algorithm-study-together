# {994}. {Rotting Oranges}

**Link:** https://leetcode.com/problems/rotting-oranges/

**Difficulty:** Medium

**Topic:** Staff, Array, Breadth-First Search, Matrix

## Problem Summary
return the minimum number of minutes that must elapse until no cell has a fresh orange.

## Approaches & Discussion
### Angela

- **So this problem is asking me to** return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
- Since we must visit every cell at least once, O(m*n) is already optimal.
- Now, Let's look at the code which I implemented.
- **My approach is to** use queue by using BFS. At first, find all rotten oranges in the matrix and append to queue and find all fresh oranges in the matrix and count. Next, while iterating over the queue, pop all cells at the same level and check their left, right, top, bottom cells whether they are fresh or not. If it is fresh, decrement the fresh count and change the state and append to the queue also using a flag variable to track whether any orange rotted during the current minute, so we know when a minute has elapsed. After this process, if the flag is True, increment the time variable. Lastly, if the fresh oranges still exist, return -1 otherwise return the time