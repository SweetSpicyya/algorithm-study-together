# {994}. {Rotting Oranges}

**Link:** https://leetcode.com/problems/rotting-oranges/
**Difficulty:** Medium
**Topic:** Staff, Array, Breadth-First Search, Matrix, Weekly Contest 124

## Approaches & Discussion

### Rachel

- **Understand**: We're given a grid with empty cells (0), fresh oranges (1), and rotten oranges (2). Every minute, rotten oranges spread to adjacent fresh oranges in 4 directions simultaneously.
- **Match**: This is a multi-source BFS problem. Instead of starting from one source, we start from all rotten oranges at once. Each BFS level represents one minute passing.
- **Plan**: First I scan the grid to push all rotten oranges into the queue and count fresh oranges. Then I run BFS level by level. For each rotten orange, I check 4 directions and rot any adjacent fresh orange and adding it to the queue. After BFS, if fresh is still greater than 0, some oranges were unreachable so I return -1.
- **Evaluate**:
  Time: O(m*n) - every cell is visited at most once
  Space: O(m*n) - queue can hold all cells in the worst case
