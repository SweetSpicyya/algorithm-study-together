# {110}. {Balanced Binary Tree}

**Link:** https://leetcode.com/problems/balanced-binary-tree/
**Difficulty:** Easy
**Topic:** Tree, Depth-First Search, Binary Tree

## Problem Summary

Determine if given binary tree is height-balanced

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by identifying patterns based on the number of nodes and the position of null values in the array.
- **Optimization**: Instead of computing height and balance check separately, I combined both into a single DFS traversal using a helper function getHeight(). The key insight is using -1. Normally getHeight() returns the actual height of a subtree, but when imbalance is detected, it immediately returns -1 as an error signal. If either left or right is -1, we propagate -1 upward.
- **Complexity Analysis**: Time Complexity: O(n) - each node is visited exactly once during the DFS traversal
  Space Complexity: O(h) = the call stack grows as deep as the height of the tree, where h is O(log n) for a balanced tree and O(n) in the worst case
