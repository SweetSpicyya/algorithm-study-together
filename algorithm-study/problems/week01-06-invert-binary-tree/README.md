# {226}. {Invert Binary Tree}

**Link:** https://leetcode.com/problems/invert-binary-tree/  
**Difficulty:** Easy
**Topic:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Problem Summary
Invert the binary tree, and return its root.

## Approaches & Discussion
### Yourim
- **Coding interview**:
  For this problem, I decided to take an iterative approach using Breadth-First Search (BFS) to traverse the tree level by level.
  First, I handle the edge case: if the root is null. I simply return null.
  To implement BFS, I use a deque to manage the nodes.
  I start by pushing the root into the queue. While queue is not empty, I dequeue the current node and swap its left and right children.
  After the swap, if the children exist, I add them the queue so they can be processed in the next iteration.
  This ensure that every single node in the tree is visited and inverted.
  Finally, once the traversal is complete, I return the original root which now points to the fully inverted tree. 
  The time complexity for this approach is O(N) and the space complexity id O(N) in the worst case due to the queue.

