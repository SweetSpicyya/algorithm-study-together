# {994}. {Rotting Oranges}

**Link:** https://leetcode.com/problems/rotting-oranges
**Difficulty:** Medium
**Topic:** Staff, Array, Breadth-First Search, Matrix, Weekly Contest 124

## Approaches & Discussion
### Yourim
Goal: Find the minimum minutes required to rot all fresh oranges, where rot spreads simultaneously in four directions.
The Flaw of Loops: A sequential nested loop causes a cascade effect where an orange rots and immediately infects its neighbor within the same minute pass.
The Solution: Use a Queue to process all currently rotten oranges simultaneously, advancing the timer layer-by-layer.
Initialization: Scan the grid first to count all fresh oranges and push all initial rotten orange coordinates into the queue.
Pop a rotten orange, check its 4 neighbors, turn fresh oranges into rotten ones, and push them into the queue for the next minute.
Termination: Return the total minutes if the fresh orange count reaches zero. otherwise, return -1 if any isolated fresh oranges remain.
Complexity: Both time and space complexities are O(MXN) because every cell is visited a constant number of times.