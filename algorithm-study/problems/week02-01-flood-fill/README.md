# {733}. {Flood Fill}

**Link:** https://leetcode.com/problems/flood-fill/
**Difficulty:** Easy
**Topic:** Mid Level, Array, Depth-First Search, Breadth-First Search, Matrix, Weekly Contest 60

## Problem Summary

Return the modified image after performing the flood fill.

## Approaches & Discussion

### Angela

- **Understand** : So the problem is asking me to modify image after performing the flood fill.
- **Brute force & Better way**: The natural approach for this problem is DFS since we need to explore adjacent pixels which runs in O(n^2)
- **Approach**: My approach is to explore each pixel that is directly adjacent using dfs function recursively and if current pixel is out of the range or not the same as the color of starting pixel, return. Also, if the color value of the starting pixel is the same as the new color, return image.
- **Complexity** : This runs in O(n^2) time complexity because this approach visits every pixel once in the worst case and O(n^2) space complexity since the call stack can grow up to n\*m in the worst case

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
  We can just keep diving into the four neighbors as long as they match the starting color.
  I've already drafted a version of this, and it works great for standard cases.
  Wait, I should consider the constraints. If the image is massive like a 1,000 X 1,000 grid, this recursive
  DFS might hit a RecursionError in Python. The call stack could get pretty deep
  if the blob we're filling is shaped like a long snake, In an interview or a production environment, that's a bit risky.
  To make this more production ready, I'd probably switch to an iterative BFS using a queue.
  It's much safer in terms of memory because we're not stacking function calls.
  Instead, we're just managing oru own queue in the heap.
  The time complexity stays the same at O(MXN), but it's way more stable for large inputs.

  # {733}. {Flood Fill}

**Link:** https://leetcode.com/problems/flood-fill/description/
**Difficulty:** Easy
**Topic:** Mid Level, Array, Depth-First Search, Breadth-First Search, Matrix, Weekly Contest 60

## Problem Summary

Fill adjacent pixels with the same color

## Approaches & Discussion

### Rachel

- **My way**: Check if the adgacent pixels have the same value and then check their neighbors before changing the color
- **Better answer**: The pronlem asks us to find all pixels that are 4-directionally connected to the starting pixel and have the same initial color. First, store the color of the starting pixel image[sr][sc] as the target color. If the target color is already the same as the new color, return the image immediately to avoid an infinite loop. Use Depth-First Search to visit each neighbor. For each pixel, check if it's within the grid boundaries and matches the target color. If it matches, update it to the new color and repeart the process for its neighbors.
