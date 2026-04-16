# {226}. {Invert Binary Tree}

**Link:** https://leetcode.com/problems/invert-binary-tree/description/
**Difficulty:** Easy
**Topic:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Problem Summary

Invert the binary tree, and return its root.

## Approaches & Discussion

### Rachel

- **Approach**: Level-order Traversal and Child Swapping
- **My way**: Dividing the tree into levels based on powers of 2 and reversing each segment. However this only works for perfect binary tree. If trees have many null nodes, converting to an array is inefficient in terms of memory.
- **Better way**: Swap the left and right children of each node and using recursion for repetitive swaping with each node's children


### Angela

- **Understand** : So the problem is asking me to invert binary tree.
- **Approach**: My approach is to use BFS traversal because it allows me to traverse nodes level by level and swap left and right children at each node.
- **Brute force**: The brute force way would be to create a new tree.
- **Better way** : We can optimize this by modifying the tree in-place.
- **Complexity** : This runs in O(n) time complexity because this approach visits every node in the tree and O(n) space complexity because given that the total number of nodes is n, the queue can hold maximum n/2 nodes at last level.








