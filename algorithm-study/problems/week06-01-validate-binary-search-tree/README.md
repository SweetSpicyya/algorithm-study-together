# {98}. {Validate Binary Search Tree}

**Link:** https://leetcode.com/problems/validate-binary-search-tree/
**Difficulty:** Medium
**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Approaches & Discussion

### Rachel

- **Understand**: We're given the root pf a binary tree and need to verify if it's a valid BST. The key insight is that every node in the left subtree must be smaller than the root, and every node in the right subtree must be larger.
- **Match**: This is a DFS problem where we pass down a valid range (mon, max) for each node. Every node must satisfy min < node.val < max. When we go left, the current node's value becomes the new max. When we go right, the current node's value becomes the new min.
- **Plan**: I'll use a recursive DFS helper that take min and max bounds. Starting with (-Infinity, Infinity) at the root, I check if the current node's value is within bounds. Then I recurse left with (min, node.val) and right with (node.val, max). If any node violates its bounds, I return false immediately.
- **Evaluate**:
  Time: O(n) - every node is visited exactly once
  Space: O(h) - call stack depth equals tree height, O(log n) for balanced tree, O(n) worst case for skewed tree.
