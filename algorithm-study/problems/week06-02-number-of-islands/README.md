# {200}. {Number of Islands}

**Link:** https://leetcode.com/problems/number-of-islands
**Difficulty:** Medium
**Topic:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Approaches & Discussion

### Rachel

- **Understand**: We're given a 2D grid of '1's (land) and '0's(water) and need to count the number of islands.
- **Match**: This is a classic DFS graph traversal problem. Each '1' cell is a node, and edges connect adjacent '1's horizontally and vertically. When we find an unvisited '1', we DFS to mark all connected '1's as visited by converting them to '0', then increment the island count.
- **Plan**: I'll iterate through every cell in the grid. When I find a '1', I increment the count and call DFS to flood-fill all connected '1's to '0'. The DFS checks four directions and stops then it hits '0' or goes out of bounds. Converting visited cells to '0' eliminates the need for a separate visitied array.
- **Evaluate**:
  Time: O(m*n) - every cess is visited at most twice
  Space: O(m*n) - call stack depth in worst case where entire grid is land
