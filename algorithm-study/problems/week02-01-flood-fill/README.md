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
- **Complexity** : This runs in O(n^2) time complexity because this approach visits every pixel once in the worst case and O(n^2) space complexity since the call stack can grow up to n*m in the worst case


