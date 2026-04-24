# {235}. {Lowest Common Ancestor of a Binary Search Tree}

**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
**Difficulty:** Medium
**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Problem Summary

Find the lowest common ancestor node of two given nodes in Binary Search Tree

## Approaches & Discussion

### Rachel

- **Clarification & Constraints**: Ask Constraints like
  What is the expected size of the input?(Scale),
  Are there any constraints on the values?(Data Range),
  Can the node values be negative or duplicates?(Data type),
  Should I conseder cases where p or q might not exist in the tree?(Edge Cases)
- **Brute-force / Initial Approach**: My initial approach would be visually reconstructing the tree but I noticed this might lead to unnecessaty space complexity.
- **Optimization**: To optimize this, I can leverage the BST property. Since p and q must eventually diverge, the LCA is simply the first split point.
- **Complexity Analysis**: This optimized approach gives me a time complexity of O(h), where h is the height of the tree
