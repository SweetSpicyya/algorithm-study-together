# {733}. {Flood Fill}

**Link:** https://leetcode.com/problems/flood-fill/  
**Difficulty:** Easy
**Topic:** Mid Level, Array, Depth-First Search, Breadth-First Search, Matrix, Weekly Contest 60

## Problem Summary
Change starting pixel's color and perform the same process for each pixel that is directly adjacent 
and shares the same color as the starting pixel.

## Approaches & Discussion
### Yourim
- **Coding interview**:
  I've got the problem. We need to change the color of a starting pixel and all its connected neighbors
  with the same original color.
  My first thought is a simple brute force scanning the whole grid but that's obviously overkill since 
  we only care about the connected component.
  So, a more targeted approach would be using DFS. It's very intuitive to implement with recursion.
  We can just keep diving into the four neighbors as long as  they match the starting color. 
  I've already drafted a version of this, and it works great for standard cases.
  Wait, I should consider the constraints. If the image is massive like a 1,000 X 1,000 grid, this recursive
  DFS might hit a RecursionError in Python. The call stack could get pretty deep 
  if the blob we're filling is shaped like a long snake, In an interview or a production environment, that's a bit risky.
  To make this more production ready, I'd probably switch to an iterative BFS using a queue.
  It's much safer in terms of memory because we're not stacking function calls.
  Instead, we're just managing oru own queue in the heap.
  The time complexity stays the same at O(MXN), but it's way more stable for large inputs.