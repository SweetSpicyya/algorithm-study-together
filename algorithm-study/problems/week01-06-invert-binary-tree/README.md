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
